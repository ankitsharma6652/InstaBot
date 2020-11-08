
username='your_username'
password='your_password'
import time
# from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
import random
driver=webdriver.Chrome(executable_path=r"C:\All Drivers\chromedriver.exe")
pic_hrefs=[]
# from selenium.webdriver.chrome.options import Options
def login():
     #Path to Chrome Driver
    driver.get('https://www.instagram.com/')
    time.sleep(2) # Wait for 5 seconds, so that you can see something.
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
# driver.get("https://www.instagram.com/explore/tags/coding/")
# driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    notNowButton = WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
    notNowButton .click()
    time.sleep(2)

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='aOOlW   HoLwm ']"))).click()
    notNowButton = WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
    notNowButton .click()
def autoLike():
    
# while True:
    hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                'newyork', 'artsy', 'alumni', 'lion', 'best', 'pythonprogramming', 'happy',
                'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
                'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                'street', 'canon', 'flutter', 'studio', 'java', 'rapsong','vintage', 'fierce','coding','python']
    driver.get('https://www.instagram.com/explore/tags/' + random.choice(hashtags) + "/")
    for _ in range(1,20):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
                # get tags
            hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
        # print(pic_hrefs)
        except Exception as e:
            continue
    for pic in pic_hrefs:
        driver.get(pic)
    # time.sleep(2)
    
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # time.sleep(2)
        try:
            time.sleep(random.randint(2, 4))
    # like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]')
            like_button = driver.find_element_by_css_selector('#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
    # driver.find_element_by_class_name("_8-yf5 ").click()
            like_button.click()
        # driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span/svg').click()
    # actionChains = ActionChains(driver)
    # actionChains.double_click(pic).perform()

        except Exception as e:
            continue
    time.sleep(60*60)
    driver.quit()
if __name__=='__main__':
    login()
    autoLike()