/* Confluence 렌더링 테스트용 외부 JS.
   docs/test.html 의 T10(외부 script src) 항목이 이 파일을 불러온다.
   실행되면 대상 글자가 "통과"로 바뀐다. */
(function () {
  var el = document.getElementById("t10-target");
  if (el) {
    el.innerHTML =
      '<span style="color:#0b8043;font-weight:700;">통과 — 외부 스크립트가 실행되었습니다</span>';
  }
})();
