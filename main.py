from selenium import webdriver
import undetected_chromedriver as uc
import time , os , pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class main:
    def __init__(self,count,gender,id,country):
        self.count,self.gender,self.country = count,gender,country
        self.id = id
        self.Initialize()

    def Initialize(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-popup-blocking')
        self.path = os.getcwd()+'/Kiabar Elmajal Cookies & Access'
        self.path2 = os.getcwd()+'/Kibar Almajal Ad Name Changer'
        options.add_argument(f'--load-extension={self.path},{self.path2}')
        self.browser = uc.Chrome(use_subprocess=True,options=options)
        self.actions = ActionChains(self.browser)
        self.browser.get('https://www.facebook.com/')
        input('<> Are You Opened Account"s?')
        self.first(self.browser)

    def first(self,browser):
        self.browser = browser
        x = self.browser.window_handles
        for i in range(len(x)):
            age = input('[ First Age , Third Age ]\n[!] Write With Comma\n<> ')
            self.age = age
            try:
                self.browser.switch_to.window(self.browser.window_handles[i])
                self.browser.implicitly_wait(60)
                self.browser.get('https://business.facebook.com/adsmanager/manage/campaigns?global_scope_id=949335292653556&tool=MANAGE_ADS&nav_entry_point=bm_global_nav_shortcut&nav_source=no_referrer&nav_id=2850714772&act=651680183133661')
                input('Press any key...')
                self.active = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div[1]/div[5]/div/span/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/input').click()
                # Send Price For Ads
                try:
                    self.price = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div[1]/div[5]/div/span/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/span/input')
                    self.price.send_keys(Keys.CONTROL, 'a')
                    time.sleep(2)
                    self.price.send_keys(self.count)
                except:
                    input('<> Error For Enter Price')
                # Submit Data Button
                time.sleep(1)
                self.submit = self.browser.find_element(By.XPATH, '//*[@id="ads_pe_container"]/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[2]/span/div/div/div/div/div[2]/div/div/button').click()
                self.second(self.age)
            except:
                print('[!] Error In First Page')

    def second(self,age):
        self.age = age
        try:
            # <!... Select The Page ....!>
            self.browser.implicitly_wait(1)
            self.browser.execute_script("window.scrollBy(0, 50)")
            WebDriverWait(self.browser, 60, ignored_exceptions=(ElementClickInterceptedException,)).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/span/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div"))).click()
            #self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/span/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div').click()
            self.browser.implicitly_wait(0.5)
            try: 
                self.swtich = self.browser.find_element(By.XPATH, f'//*[@id="{self.id}"]/div/div').click()
            except:
                for i in range(4,11):
                    try:
                        self.swtich = self.browser.find_element(By.XPATH, f'/html/body/div[{i}]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div').click()
                        break
                    except:
                        pass
            # <!... Country Settings ....!>
            try:
                for i in range(3,11):
                    try:
                        self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[{i}]/div/div/div/div/div/div[2]/div/div/div[2]/div/div').click()
                        break
                    except:
                        pass
                self.remove_current = self.browser.find_element(By.XPATH, '//*[@id="LOCATION"]/div[2]/div[1]/ul/li/ul/li[2]/ul/li/div/div[4]/span').click()
                time.sleep(1)
                for search in range(1,10):
                    try:
                        self.search_country = self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[{search}]/div[2]/div/span/label')
                        self.search_country.send_keys(self.country)
                        time.sleep(3)    
                        self.actions.send_keys(Keys.RETURN)
                        self.actions.perform()
                        break
                    except:
                        pass
            except:
                print('[!] Error For Choice Country')
                input('Please Remove Thats you')
            # <!... Age ....!>
            # Open Menu Num1
            try:
                try:
                    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[5]/div/div/div/div/div/div[2]/div/div/div[2]/div/div').click()
                except:
                    input('Path Changed اقفش')
                self.num1 , self.num2 = self.age.split(',')
                if int(self.num1) == 18:
                    pass
                else:
                    for i in range(2,10):
                        try:
                            self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[{i}]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div').click()
                            break
                        except:
                            pass
                    for j in range(3,11):
                        try:
                            self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[{j}]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[{int(int(self.num1)-17)}]/div').click()
                            break
                        except:
                            pass
                # Open Menu Number2
                self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[4]/div').click()
                
                for kk in range(2,10):
                    try:
                        self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[{kk}]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[{int(int(self.num2)-17)}]/div').click() 
                        break
                    except:
                        pass
            except:                                 
                input('<> Error For Age Select Them With YourSelf: ')

            # <!... Gender Settings ...!>
            try:
                if self.gender == 'M':
                    # Open Editor
                    try:
                        try:
                            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div[2]/div/div').click()
                        except:
                            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div[2]/div/div').click()
                        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/input').click()
                    except:
                        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/input').click()
                elif self.gender == 'F':
                    # Open Editor
                    try:
                        try:
                            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div[2]/div/div').click()
                        except:
                            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div[2]/div/div').click()
                        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div[1]/div/input').click()
                    except:
                        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[6]/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div[1]/div/input').click()
                elif self.gender == 'A' or self.gender == 'a':
                    pass
            except:
                print('<> Error To Change Gender')
            # < Last Settings >
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/label[2]/div/div/div[1]/div/div/div[1]/input').click()
            try:
                time.sleep(0.5)
                try:
                    edit_button = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div").click()
                except:
                    pass
                # Open Menu 
                WebDriverWait(self.browser, 60, ignored_exceptions=(ElementClickInterceptedException,)).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div"))).click()
                # Remove Computer
                for computer in range(3,10):
                    try:
                        self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[{computer}]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[2]/div').click()
                    except:
                        pass
            except:
                print('<> Error To Remove Computer Value')
                input('Please Remove Thats you')
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div').click()    
            try:
                #remove Audince Network
                try:
                    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/ul/table[2]/tbody/tr/td[1]/td/li/div/div/div/input').click()
                except:
                    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/ul/table[2]/tbody/tr/td[1]/li/div/div/div/input').click()
                #remove Messenger
                try:
                    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/ul/table[2]/tbody/tr/td[2]/td/li/div/div/div/input').click()
                except:
                    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/ul/table[2]/tbody/tr/td[2]/li/div/div/div/input').click()
                #remove Instagram
                try:
                    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/ul/table[1]/tbody/tr/td[2]/td/li/div/div/div/input').click()
                except:
                    self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/ul/table[1]/tbody/tr/td[2]/li/div/div/div/input').click()
            except:
                print('Error in Last Settings')
                input('Please Remove Thats you')
            time.sleep(0.5)
            # Submit Data 
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[2]/span/div/div/div/div/div[2]/div/div[2]/button').click()
             
            # Third Page
            self.browser.execute_script("window.scrollBy(0, 50)")
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/span/div/div[1]/div[2]/div/div/div/div/div/div[1]').click()
            try:

                self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/span/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div').click()
            except:
                self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div[2]/div/div[2]/span[1]/div/div[3]/div/div[2]/div/span/div/div/div[1]/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/span/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div').click()
            input('Finally\nYou Are Finished')
            
        except:
            print('<> Error In Second Page')
            input('Press any key..')


if __name__ == '__main__':
    count = input('[ Enter The Prise For ones ]\n<> ')
    gender = input('[ Select The Gender ]\nM ==> male \nF ==> Female\n<> ').capitalize()
    id_page = input('[ Enter ID Page ]\n<> ')
    country = input('[ Enter The Country ]\n<> ')
    start = main(count,gender,id_page,country)
