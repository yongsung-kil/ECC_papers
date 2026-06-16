// LDPC 논문 1차 선별 — 병렬 워크플로
//
// 메인(오케스트레이터)이 `python -m src.review batch`로 미선별 논문을
// 에이전트별 파일(_batch/agent_NN.json)로 분할한 뒤 이 워크플로를 실행한다.
// 각 에이전트는 자기 파일 1개만 읽어 in/out 판정하고, 메인이 결과를 모아 DB에 기록한다.
//
// 실행: Workflow({ scriptPath: "select_workflow.js",
//                  args: { dir: "_batch", nAgents: N, criteriaFile: "criteria/selection_criteria.md" } })

export const meta = {
  name: 'select-ldpc',
  description: 'LDPC 논문을 NAND 적용 가능성으로 병렬 선별 (in/out + 기준제안 + 경계사례)',
  phases: [{ title: 'Judge', detail: '에이전트별로 담당 논문 in/out 판정' }],
}

// ── 파라미터 (args로 덮어쓰기 가능) ───────────────────────────────
const DIR           = (args && args.dir) || '_batch'
const N_AGENTS      = (args && args.nAgents) || 0
const CRITERIA_FILE = (args && args.criteriaFile) || 'criteria/selection_criteria.md'
// ─────────────────────────────────────────────────────────────────

const SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['judgments', 'criteria_suggestions', 'borderline'],
  properties: {
    judgments: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['id', 'decision', 'reason'],
        properties: {
          id: { type: 'string' },
          decision: { type: 'string', enum: ['in', 'out'] },
          reason: { type: 'string' },
        },
      },
    },
    criteria_suggestions: { type: 'array', items: { type: 'string' } },
    borderline: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['id', 'note'],
        properties: { id: { type: 'string' }, note: { type: 'string' } },
      },
    },
  },
}

if (!N_AGENTS) {
  log('판정할 배치가 없습니다 (nAgents=0).')
  return { judgments: [], criteria_suggestions: [], borderline: [] }
}

function agentPrompt(idx) {
  const file = DIR + '/agent_' + String(idx).padStart(2, '0') + '.json'
  return [
    '너는 LDPC 논문 1차 선별자다. NAND 플래시 LDPC ECC 적용 가능성으로 논문을 in/out 판정한다.',
    '',
    '1) `' + CRITERIA_FILE + '` 를 읽어 선별 기준(포함/제외 카테고리·판단절차)을 숙지한다.',
    '2) `' + file + '` 를 읽는다 — 담당 논문 JSON 배열(id, title, abstract 등).',
    '3) 각 논문을 초록만 보고 판정한다.',
    '',
    '반환(StructuredOutput):',
    '- judgments: 담당 논문 전부 [{id, decision:"in"|"out", reason: 한 줄}]',
    '- criteria_suggestions: 기준(in/out·판단절차)을 바꿀 만한 게 보일 때만 문자열 배열. 없으면 [].',
    '- borderline: 판정이 애매했던 논문만 [{id, note}]. 애매하면 in으로 살리고 여기 기록. 없으면 [].',
  ].join('\n')
}

phase('Judge')
const results = await parallel(
  Array.from({ length: N_AGENTS }, (_, idx) => () =>
    agent(agentPrompt(idx), { label: 'judge:' + idx, phase: 'Judge', schema: SCHEMA })
  )
)

const judgments = []
const criteria_suggestions = []
const borderline = []
for (const r of results) {
  if (!r) continue
  judgments.push(...(r.judgments || []))
  criteria_suggestions.push(...(r.criteria_suggestions || []))
  borderline.push(...(r.borderline || []))
}

log('판정 ' + judgments.length + '편 · 기준제안 ' + criteria_suggestions.length +
    ' · 경계 ' + borderline.length)
return { judgments, criteria_suggestions, borderline }
