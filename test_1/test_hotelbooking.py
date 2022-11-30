from POM.hotel_booking import HotelPage

class TestHotelPage:
    def test_hotel(self, _driver):
        hotel = HotelPage(_driver)
        hotel.popup()
        hotel.click_hotel()
        hotel.destination()
        hotel.dropdown()
        hotel.date()
        hotel.sel_dropdown()
        hotel.button()
        hotel.book_button()
        hotel.continue_button()
        hotel.enter_mob()
        hotel.enter_email()
        hotel.button_continue()
        hotel.title_click()
        hotel.text_title()
        hotel.enter_firstname()
        hotel.enter_lastname()
        hotel.payment_btn()
