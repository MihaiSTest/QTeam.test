from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://magento.softwaretestingboard.com")

def wait_for_element(strategy, value, max_wait=10):
    start_time = time.time()
    while time.time() - start_time < max_wait:
        try:
            element = driver.find_element(strategy, value)
            if element.is_displayed():
                return element
        except Exception as e:
            pass
        time.sleep(1)
    raise TimeoutError(f"Timed out after {max_wait} seconds waiting for element {strategy}: {value}")

def select_dropdown_item(driver, dropdown_locator, item_text):
   
    dropdown = driver.find_element(*dropdown_locator)

    select = Select(dropdown)

    select.select_by_visible_text(item_text)

wait_for_element(By.ID, "option-label-size-143-item-166").click()
wait_for_element(By.ID, "option-label-color-93-item-57").click()
wait_for_element(By.CLASS_NAME, "action.tocart.primary").click()
wait_for_element(By.CLASS_NAME, "counter.qty").click()
wait_for_element(By.CLASS_NAME, "action.primary.checkout").click()

wait_for_element(By.ID, "customer-email").send_keys("mihai.test@email.com")
wait_for_element(By.NAME, "firstname").send_keys("mihai")
wait_for_element(By.NAME, "lastname").send_keys("mihaistefan")
wait_for_element(By.NAME, "company").send_keys("test")
wait_for_element(By.NAME, "street[0]").send_keys("test")
wait_for_element(By.NAME, "city").send_keys("Craiova")
select_dropdown_item(driver, (By.NAME, "country_id"), "Romania")
select_dropdown_item(driver, (By.NAME, "region_id"), "Dolj")
wait_for_element(By.NAME, "postcode").send_keys("200300")
wait_for_element(By.NAME, "telephone").send_keys("+40799123456")

time.sleep(5)
wait_for_element(By.CLASS_NAME, "button.action.continue.primary").click()
time.sleep(5)
wait_for_element(By.CLASS_NAME, "action.primary.checkout").click()

confirmation_message = wait_for_element(By.CLASS_NAME, "base").text
assert "Thank you for your purchase!"

driver.quit()