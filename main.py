import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def handler(event=None, context=None):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/opt/chrome/chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    chrome_options.add_argument('window-size=1392x1150')
    chrome_options.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path="/opt/chromedriver", options=chrome_options)

    print("browser", browser)

    browser.get("https://www.naver.com/")
    description = browser.find_element(By.NAME, "description").get_attribute("content")

    print(description)

    browser.close()

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": description,
            }
        ),
    }

if __name__ == '__main__':
    handler()