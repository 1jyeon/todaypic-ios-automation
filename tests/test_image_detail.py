from pages.image_detail_page import ImageDetailPage

def test_image_detail_open(driver):
    picker_page = ImageDetailPage(driver)
    
    assert picker_page.is_detail_cancel_displayed(), "다이얼 아래 취소가 표시되지 않았습니다."