from pages.picker_page import PickerPage
from pages.calendar_page import CalendarPage

def test_picker_open(driver):
    ## TC-PICKER_DIALOG-001##
    picker_page = PickerPage(driver)
    calender_page = CalendarPage(driver)
    calender_page.click_header()

    assert picker_page.BTN_PICKER_CANCEL(), "다이얼 아래 취소가 표시되지 않았습니다."
    assert picker_page.BTN_PICKER_CONFIRM(), "다이얼 아래 이동이 표시되지 않았습니다."

def test_calendar_picker_navigation(driver):
    ## TC-PICKER_DIALOG-002##
    picker_page = PickerPage(driver)
    calender_page = CalendarPage(driver)
    target_y = "25년"
    target_m = "11월"
    picker_page.select_year_and_month(target_y, target_m)
    header_date = calender_page.HEADER_DATE.text
    assert header_date!=picker_page.select_year_and_month(target_y, target_m), "picker에 25년 11월이 정상적으로 이동되지 않았습니다."