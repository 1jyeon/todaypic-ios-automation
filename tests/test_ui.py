from pages.calendar_page import CalendarPage

def test_verify_main_calendar_ui(driver):
    calendar_page = CalendarPage(driver)

    assert calendar_page.is_header_date_displayed(), "해당 년도와 날짜가 보이지 않습니다."
    assert calendar_page.is_today_button_enabled(), "'오늘' 버튼이 비활성 상태입니다."
    assert calendar_page.is_add_button_displayed(), "추가(+) 버튼이 보이지 않습니다."

def test_sunday_color_is_red(driver):
    calendar_page = CalendarPage(driver)
    r, g, b = calendar_page.get_element_color(calendar_page.SUNDAY_LABEL)   

    assert r > 200 and g < 150, f"일요일 색상이 예상과 다릅니다. (R:{r}, G:{g})"

def test_saturday_color_is_blue(driver):
    calendar_page = CalendarPage(driver)
    r, g, b = calendar_page.get_element_color(calendar_page.SATURDAY_LABEL)

    assert b > 200 and r < 150, f"토요일 색상이 파란색이 아닙니다. (B:{b})"

def test_open_date_picker_dialog(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.click_header()
  
    assert calendar_page.is_picker_move_button_displayed(), "날짜 선택 다이얼이 열리지 않았습니다."

def test_swipe_before_calendar(driver):
    calendar_page = CalendarPage(driver)
    before_month = calendar_page.get_current_month_text()
    calendar_page.swipe_calendar(direction="right")
    after_month = calendar_page.get_current_month_text()       

    assert before_month!=after_month, "스와이프 후에 달이 변경되지 않았습니다"

def test_swipe_after_calendar(driver):
    calendar_page = CalendarPage(driver)
    before_month = calendar_page.get_current_month_text()
    calendar_page.swipe_calendar(direction="left")
    after_month = calendar_page.get_current_month_text()       

    assert before_month==after_month, "스와이프 후에 달이 변경되었습니다"