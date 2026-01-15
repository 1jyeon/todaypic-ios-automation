# Wheel Date Picker 테스트 케이스

## TC-PICKER_DIALOG-001
- 목적: Wheel Date Picker 버튼 여부 확인
- 사전조건:
  - 앱 실행 완료
- 테스트 데이터:
  - BTN_PICKER_CANCEL: Y
  - BTN_PICKER_CONFIRM: Y
- 수행 절차:
  1. PICKER 화면 이동
  2. BTN_PICKER_CANCEL, BTN_PICKER_CONFIRM 버튼 표시 확인
- 기대 결과:
  - 버튼 표시됨 확인
---

## TC-PICKER_DIALOG-002
- 목적: Wheel Date Picker로 선택한 날짜와 좌측 상단 날짜 텍스트가 동일한지 여부 확인
- 사전조건:
  - 앱 실행 완료
  - Wheel Date Picker 화면 이동
- 테스트 데이터:
  - target_y: 25년
  - target_m: 11월
- 수행 절차:
  1. 날짜를 25년 11월로 변경
  2. 이동시 좌측 상단 날짜 텍스트 확인
- 기대 결과:
  - 25년 11월 확인
---