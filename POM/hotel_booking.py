from Data import reading_objects
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

hotel_obj = reading_objects.read_locators()
print(hotel_obj)

class HotelPage:
    def __init__(self,driver):
        self.driver=driver

    def popup(self):
        self.driver.find_element(*hotel_obj['text_popup']).click()

    def click_hotel(self):
        self.driver.find_element(*hotel_obj['text_hotel']).click()

    def destination(self):
        place = self.driver.find_element(*hotel_obj['text_location'])
        place.click()
        place.send_keys("The Orchid Hotel Mumbai Vile Parle, Mumbai,Maharashtra, India")
        time.sleep(4)

    def dropdown(self):
        self.driver.find_element(*hotel_obj['text_dropdown']).click()

    def date(self):
        self.driver.find_element(*hotel_obj['text_fromdate']).click()
        time.sleep(1)
        self.driver.find_element(*hotel_obj['click_startdate']).click()
        time.sleep(1)

        # self.driver.find_element(*hotel_obj['text_todate']).click()
        # time.sleep(10)
        self.driver.find_element(*hotel_obj['click_enddate']).click()
    

    def sel_dropdown(self):
        self.driver.find_element(*hotel_obj['select_dropdown']).click()
        self.driver.find_element(*hotel_obj['opt_dropdown']).click()
        self.driver.find_element(*hotel_obj['click_addroom']).click()
        self.driver.find_element(*hotel_obj['addroom_travellers']).click()
        self.driver.find_element(*hotel_obj['increase_child']).click()
        self.driver.find_element(*hotel_obj['page_click']).click()

    def button(self):
        self.driver.find_element(*hotel_obj['search_btn']).click()
        wait_obj = WebDriverWait(self.driver, 30)
        wait_obj.until(expected_conditions.presence_of_element_located(("xpath", "//div[@class='flex flex-nowrap']")))
        sel_btn = self.driver.find_element(*hotel_obj['select_btn'])
        obj_1 = ActionChains(self.driver)
        obj_1.move_to_element(sel_btn).perform()

        obj_1 = ActionChains(self.driver)
        obj_1.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    def book_button(self):
        self.driver.find_element(*hotel_obj['book_btn']).click()

        handles = self.driver.window_handles
        print(handles)
        print(handles[1])
        time.sleep(10)
        self.driver.switch_to.window(handles[1])

        obj_2 = ActionChains(self.driver)
        obj_2.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    def continue_button(self):
        self.driver.find_element(*hotel_obj['continue_btn']).click()

    def enter_mob(self):
        self.driver.find_element(*hotel_obj['text_mob']).send_keys("9765433425")

    def enter_email(self):
        self.driver.find_element(*hotel_obj['text_email']).send_keys("admin123@gmail.com")

    def button_continue(self):
        self.driver.find_element(*hotel_obj['btn_continue']).click()

    def title_click(self):
        self.driver.find_element(*hotel_obj['click_title']).click()

    def text_title(self):
        self.driver.find_element(*hotel_obj['text_title']).click()

    def enter_firstname(self):
        self.driver.find_element(*hotel_obj['text_firstname']).send_keys("Abc")

    def enter_lastname(self):
        self.driver.find_element(*hotel_obj['text_lastname']).send_keys("xyz")
        obj_1 = ActionChains(self.driver)
        obj_1.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    def payment_btn(self):
        self.driver.find_element(*hotel_obj['payment_btn']).click()
        # pay.click()



# hotel = HotelPage()
# hotel.popup()
# hotel.click_hotel()
# hotel.destination()
# hotel.dropdown()
# hotel.date()
# hotel.sel_dropdown()
# hotel.button()
# hotel.book_button()
# hotel.continue_button()
# hotel.enter_mob()
# hotel.enter_email()
# hotel.button_continue()
# hotel.title_click()
# hotel.text_title()
# hotel.enter_firstname()
# hotel.enter_lastname()
# hotel.payment_btn()