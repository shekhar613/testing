from cgi import test
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os
import pickle

load_dotenv()

# add chromewebdriver path 
path = r'.\chromedriver.exe'

test_url = 'https://www.instagram.com/p/Cbu2qwNJaSf/?utm_medium=copy_link'

class Scrap:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=path)
    
    def login(self):
        self.driver.get('https://instagram.com')

        sleep(2)

        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

        inputs[0].send_keys(os.getenv('user'))
        inputs[1].send_keys(os.getenv('password'))
        submit_btn.click()

        sleep(5)

        pickle.dump(self.driver.get_cookies(), open("cookies.pkl","wb"))

    
    def get(self, url):
        try:        
            self.driver.get(url)

            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()

            sleep(2)

            video_ref = self.driver.find_element(By.TAG_NAME, "video")

            url = video_ref.get_attribute('src')
            self.driver.quit()

            return url
        except Exception as err:
            print(err)
            return "Something went wrong"


if __name__ == "__main__":
    a = input()
    scrap = Scrap()

    url = scrap.get(a)

    print(url)
