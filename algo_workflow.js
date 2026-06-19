// Phase 2.5 — '알고리즘 측면 수정' 재판정 (병렬 워크플로)
//
// filtered_in 중 reason 파싱으로 카테고리를 못 찾은 '애매' 논문을 대상으로,
// 각 에이전트가 초록을 읽고 알고리즘/코드 기여(keep) vs HW만(drop)을 판정한다.
//
// 실행: Workflow({ scriptPath: "algo_workflow.js",
//                  args: { dir: "<RUN_DIR>", nAgents: N } })

export const meta = {
  name: 'algo-classify',
  description: 'LDPC filtered_in 논문의 알고리즘/코드 수정 여부 재판정 (keep/drop)',
  phases: [{ title: 'Judge', detail: '에이전트별 알고리즘 vs HW-only 판정' }],
}

let ARGS = args
if (typeof ARGS === 'string') { try { ARGS = JSON.parse(ARGS) } catch (e) { ARGS = {} } }
const DIR      = (ARGS && ARGS.dir) || ''
const N_AGENTS = (ARGS && ARGS.nAgents) || 0

const SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['judgments'],
  properties: {
    judgments: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['id', 'algo', 'reason'],
        properties: {
          id: { type: 'string' },
          algo: { type: 'string', enum: ['keep', 'drop'] },
          reason: { type: 'string' },
        },
      },
    },
  },
}

if (!N_AGENTS) { log('판정할 배치가 없습니다 (nAgents=0).'); return { judgments: [] } }

function agentPrompt(idx) {
  const file = DIR + '/agent_' + String(idx).padStart(2, '0') + '.json'
  return [
    '너는 LDPC 논문 분류자다. 이 논문들은 이미 NAND LDPC ECC 적용성 1차 선별을 통과했다.',
    '이번엔 단 하나만 판정한다: 이 논문이 **알고리즘 측면의 수정(기여)** 을 담고 있는가?',
    '',
    '- keep: LDPC **디코더 알고리즘**(min-sum/BP 변형, 스케줄링 알고리즘, 신경망 디코더, OSD 등)',
    '        또는 **부호 설계/구성**(QC/SC-LDPC 구성, girth·사이클 제거, error floor, degree distribution,',
    '        protograph, 유한길이 설계 등), 또는 NAND/스토리지의 **검출·LLR·read-retry 등 알고리즘** 기여가 있음.',
    '- drop: 기여가 **하드웨어뿐**이다 — FPGA/VLSI/ASIC/CMOS 디코더·인코더 아키텍처, 회로, 메모리/배선/',
    '        파이프라인/스케줄링의 *구현* 최적화처럼, 표준 알고리즘을 HW로 구현·가속한 것에 그침.',
    '',
    '핵심 경계: "새로운 알고리즘/부호를 제안했나" = keep / "기존 알고리즘을 HW로 구현·가속만 했나" = drop.',
    '애매하면 keep.',
    '',
    '`' + file + '` 를 읽어라 — 담당 논문 JSON 배열(id, title, abstract, reason[1차 선별 근거]).',
    '각 논문을 초록 기준으로 판정한다.',
    '',
    '반환(StructuredOutput): judgments = 담당 논문 전부 [{id, algo:"keep"|"drop", reason: 한 줄}]',
  ].join('\n')
}

phase('Judge')
const results = await parallel(
  Array.from({ length: N_AGENTS }, (_, idx) => () =>
    agent(agentPrompt(idx), { label: 'algo:' + idx, phase: 'Judge', schema: SCHEMA })
  )
)

const judgments = []
for (const r of results) { if (r) judgments.push(...(r.judgments || [])) }
log('판정 ' + judgments.length + '편')
return { judgments }
