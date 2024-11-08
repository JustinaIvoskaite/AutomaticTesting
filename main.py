import time
import  helpers
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

def PlacingTheBet():
    driver.get("https://demo.betgames.tv")
    #game selection:

    iframe = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    #print(f"Number of elements found: {len(elements)}")


    button_select_skyward = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='area-game-card-27']"))
        )
    button_select_skyward.click()
    time.sleep(10)

    balance_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa='text-balance-amount']"))
    )
    balance_text = balance_element.text
    balance_value = float(balance_text.replace("€", "").replace(",", ""))
    #The placed bet:
    amount_input = driver.find_element("css selector", "[data-qa='input-bet-slip-amount']")
    amount_value = float(amount_input.get_attribute("value"))

    button_place = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa='button-place-bet']"))
    )
    button_place.click()
   #when the bet is placed:

    time.sleep(15)
    new_balance_text = balance_element.text
    new_balance_value = float(new_balance_text.replace("€", "").replace(",", ""))
    print(new_balance_value)
    print(amount_value)

    if (new_balance_value+amount_value) == balance_value:
        print("Test passed, value decreases upon placing the bet")

    else:
        print("Test failed")
    time.sleep(35)

    driver.quit()
def ContactingServiceTest():
    driver.get("https://demo.betgames.tv")
    language_first = "Lithuanian"
    language_second = "English"

    #if different selected:
    '''get_language_parent = driver.find_element(By.ID, "language")
    selected = get_language_parent.find_element(By.TAG_NAME, "a").text.strip()
    '''
    email_input =driver.find_element(By.NAME, "email")
    message_input = driver.find_element(By.NAME, "message")
    send_btn  = driver.find_element(By.CSS_SELECTOR, ".send.btn.btn-primary.pull-left")
    message_input.send_keys("Testavimo zinute")
    email_input.send_keys("kazkas@gmail.com")
    should_be = helpers.GetMessageByLanguage(language_second)
    send_btn.click()
    #message for success if sent

    success = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "send"))
    )
    got_text = success.text
    print(f"Text received: '{got_text}'")
    assert got_text == should_be, f"Message is not correct. Expected: '{should_be}', Found: '{got_text}'"



if __name__ == "__main__":
    #Verification()
    #ContactingServiceTest()
    PlacingTheBet()
