#Level 2
#IMP_001 Creating New Imports - Pickup
import random
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium_testing_library import Screen, Within
from customer_utils import login, password, user, logout

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)
screen = Screen(driver)

try:
    # Login
    login(driver, user, password)
    shipping_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/imports']"))
    )
    shipping_link.click()
    # Navigate to Imports page
    screen.get_by_test_id("sidebar-imports-item").click()
    print("** /imports clicked.")
    #endregion
    # Click on New Import button
    screen.find_by_text("New Import").click()
    # Click is not a return
    Within(screen.find_by_test_id("is-return")).get_by_role(role="radio", name="No").click()
    # Select is a package
    Within(screen.find_by_test_id("import-package-or-skid")).get_by_role(role="radio", name="Arriving as a package").click()
    # Pick up from warehouse
    screen.find_by_test_id("ship-to").click()
    screen.find_by_text("SS Markham").click()
    screen.find_by_text("No, I would like to get an estimate").click()
    screen.get_by_test_id("acknowledge-is-estimate").click()
    # Select a vendor
    Within(screen.get_by_test_id('vendor')).get_by_role('textbox').send_keys("Amazon")
    screen.find_by_text("Amazon (Warehouse Deals and Pantry)").click()
    add_packages = Within(screen.get_by_test_id("items-amount")).get_by_class_name("plus-icon")
    # Add more two packages
    add_packages.click()
    add_packages.click()
    # Scroll to the bottom of the page
    driver.execute_script("window.scroll({ top: document.documentElement.scrollHeight });")
    # Add just one product
    screen.get_by_test_id("product-condition-0").click()
    screen.find_by_text("New").click()
    screen.get_by_test_id("product-category-0").click()
    screen.find_by_text("Fan of textile").click()
    screen.get_by_test_id("country-of-origin-0").click()
    screen.find_by_text("China").click()
    Within(screen.get_by_test_id("product-quantity-0")).get_by_role("spinbutton").send_keys(1)
    Within(screen.get_by_test_id("product-value-0")).get_by_role("spinbutton").send_keys(120)
    screen.get_by_test_id("confirm").click()
    screen.get_by_text("Review Estimate").click()
    time.sleep(5)
    screen.find_by_text("Proceed: Save Estimate").click()    
    #vendor_info = screen.find_by_test_id("vendor-name").text
    #self.assertEqual(vendor_info, "") 
    time.sleep(2)
    screen.get_by_test_id("Checkbox_import1").click
    time.sleep(2)
    screen.get_by_test_id("import-item-0-chevron").click()
    time.sleep(2)
    screen.get_by_test_id("import-item-edit-icon").click()
    time.sleep(2)
    screen.get_by_text("Yes, I have a tracking number").click()
    time.sleep(2)
    textbox = screen.get_by_test_id("Carrier name")
    textbox.send_keys("Fedex")
    tracking_1 = screen.get_by_test_id("tracking_package1").send_keys(random)
    tracking_2 = screen.get_by_test_id("tracking_package2").send_keys(random)
    tracking_3 = screen.get_by_test_id("tracking_package3").send_keys(random)
    screen.get_by_test_id("confirm").click()
    screen.get_by_text("Save & Pay with other Imports").click()
    time.sleep(5)
    screen.get_by_test_id("Checkbox_import1").click()
    screen.get_by_text(" CHECKOUT").click()
    screen.get_by_test_id("terms_conditions").click()
    screen.get_by_test_id("sidebar-imports-item").click()
    screen.get_by_test_id("import-item-0-chevron").click()
    screen.get_by_test_id("delete-button").click()
    screen.get_by_text("YES, CANCEL").click()
    
    logout(driver)
    driver.quit()
except WebDriverException as e:
    print("Failed WebDriver:", e)
    driver.quit()