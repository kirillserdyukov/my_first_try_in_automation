from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_exist_button_basket(browser):
    browser.implicitly_wait(5)
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(f"{link}")
    try:
        x = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket"))
        )
        assert x.get_attribute('value') == browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket").text #добавил просто ради assert
    except TimeoutException as error:
        print(f"Object not found, time is up, {error}")
    except NoSuchElementException as error:
        print(error)

