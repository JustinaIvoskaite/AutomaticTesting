import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#Performance test,
def Verification():
    driver.get("https://demo.betgames.tv")

    driver.quit()

#for testing window size for different selections-is it a tablet, mobile or dekstop:
def TestWindowDisplay():
    driver.set_window_size()

def PerformaceTesting():
    return

def ContactingServiceTest():
    driver.get("https://demo.betgames.tv")
    email_input =driver.find_element(By.NAME("email"))
    message_input = driver.find_element(By.NAME("message"))


if __name__ == "__main__":
    Verification()
    input("Press Enter to close the browser...")
