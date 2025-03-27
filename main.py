import os
import time
import webbrowser

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import dates

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
URL = os.getenv('URL')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option('prefs', {'profile.default_content_setting_values.notifications': 2})
driver = webdriver.Chrome(options)


def main():
    if not all([EMAIL, PASSWORD, URL]):
        print('\nCheck .env')
        return

    if len(dates) == 0:
        print('\nDates are empty.')
        return

    print('\nChecking…')
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, 'input[name=email]').send_keys(EMAIL)
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[type=password]')
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(1)

    # Showtime
    for d in dates:
        check(d, '09:00', 'Check-in.')
        check(d, '18:00', 'Check-out.')

    webbrowser.open(URL + '/approvals/my-requests')
    driver.quit()


def check(date_str, time_str, note):
    driver.find_element(By.CSS_SELECTOR, '[data-url=":me/-/claim"]').click()

    date_input = driver.find_element(By.CSS_SELECTOR, 'input[data-role=date]')
    date_input.send_keys(date_str)
    time_input = driver.find_element(By.CSS_SELECTOR, 'input[data-role=time]')
    for _ in range(5): time_input.send_keys(Keys.BACK_SPACE)
    time_input.send_keys(time_str)
    driver.find_element(By.CSS_SELECTOR, 'textarea[name=content]').send_keys(note)

    driver.find_element(By.CSS_SELECTOR, '.button.ok').click()
    time.sleep(.5)


if __name__ == '__main__':
    main()
