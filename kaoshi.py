from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
from parameterized import parameterized,param
from para_csv import para_csv
import time

#登录页面
class LoginPage_OBJ():
    username=(By.ID,"inputUsername")
    passname=(By.ID,"inputPassword")
    btn=(By.XPATH,'/html/body/div/form/button')
    err=(By.XPATH,'/html/body/div/form/p')

#添加发布会页面
class LoginPage_FBH():
    tianjia=(By.XPATH,'/html/body/div/div[1]/div[2]/button')
    name=(By.XPATH,'//*[@id="id_name"]')
    address=(By.XPATH,'//*[@id="id_address"]')
    number=(By.XPATH,'//*[@id="id_limit"]')
    date=(By.XPATH,'//*[@id="id_start_time"]')
    submit=(By.XPATH,'/html/body/div[1]/div[2]/form/div[7]/div/button')

#添加嘉宾页面
class LoginPage_JIABIN():
    jiabin=(By.XPATH,'//*[@id="navbar"]/ul[1]/li[2]/a')
    tianjia01=(By.XPATH,'/html/body/div/div[1]/div[2]/button')
    fabuhui=(By.XPATH,'//*[@id="id_event"]')
    phone=(By.XPATH,'//*[@id="id_phone"]')
    email=(By.XPATH,'//*[@id="id_email"]')
    nameone=(By.XPATH,'//*[@id="id_realname"]')
    submitone=(By.XPATH,'/html/body/div[1]/div[2]/form/div[7]/div/button')

#初始化
class BasePage():
    def __init__(self,driver):
        self.driver=driver

#登录页面操作层
class LoginPage(BasePage):

    def enter_username(self,username):
        ele=self.driver.find_element(*LoginPage_OBJ.username)
        ele.clear()
        ele.send_keys(username)

    def enter_passname(self,passname):
        ele=self.driver.find_element(*LoginPage_OBJ.passname)
        ele.clear()
        ele.send_keys(passname)

    def enter_btn(self):
        ele=self.driver.find_element(*LoginPage_OBJ.btn)
        ele.click()


    def enter_err(self):
        ele=self.driver.find_element(*LoginPage_OBJ.err)

#发布会页面操作层
class Fabu_tianjia(BasePage):

    def enter_tianjia(self):
        ele=self.driver.find_element(*LoginPage_FBH.tianjia)
        ele.click()

    def enter_name(self,name):
        ele=self.driver.find_element(*LoginPage_FBH.name)
        ele.clear()
        ele.send_keys(name)

    def enter_address(self,address):
        ele=self.driver.find_element(*LoginPage_FBH.address)
        ele.clear()
        ele.send_keys(address)

    def enter_number(self,number):
        ele=self.driver.find_element(*LoginPage_FBH.number)
        ele.clear()
        ele.send_keys(number)

    def enter_data(self,date):
        ele=self.driver.find_element(*LoginPage_FBH.date)
        ele.clear()
        ele.send_keys(date)

    def click_submit(self):
        ele=self.driver.find_element(*LoginPage_FBH.submit)

#嘉宾操作页面
class Jiabin_tianjia(BasePage):
    def enter_jiabin(self):
        ele=self.driver.find_element(*LoginPage_JIABIN.jiabin)
        ele.click()

    def enter_tianjia01(self):
        ele=self.driver.find_element(*LoginPage_JIABIN.tianjia01)
        ele.click()

    def enter_fabuhui(self):
        ele=self.driver.find_element(*LoginPage_JIABIN.fabuhui)
        select=Select(ele)
        select.select_by_index(5)
        ele.click()

    def enter_phone(self,phone):
        ele=self.driver.find_element(*LoginPage_JIABIN.phone)
        ele.clear()
        ele.send_keys(phone)

    def enter_email(self,email):
        ele=self.driver.find_element(*LoginPage_JIABIN.email)
        ele.clear()
        ele.send_keys(email)

    def enter_nameone(self,nameone):
        ele=self.driver.find_element(*LoginPage_JIABIN.nameone)
        ele.clear()
        ele.send_keys(nameone)

    def enter_submitone(self,):
        ele=self.driver.find_element(*LoginPage_JIABIN.submitone)
        ele.click()

#测试用例层
data=para_csv(r"C:\Users\Administrator\Desktop\datas.csv")
print(data)
class TestLoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://150.109.156.47:8000/")
    @parameterized.expand([("admin","admin","0"),("admin","admin123456","1",)])


    def test_Login01(self,username,passname,status):
        LoginPage(self.driver).enter_username(username)
        LoginPage(self.driver).enter_passname(passname)
        LoginPage(self.driver).enter_btn()

        if status=="1":
            print("success")
            time.sleep(3)
            Fabu_tianjia(self.driver).enter_tianjia()
            Fabu_tianjia(self.driver).enter_name("苹果发布会")
            Fabu_tianjia(self.driver).enter_address("北京")
            Fabu_tianjia(self.driver).enter_number("100")
            Fabu_tianjia(self.driver).enter_data("2023-10-30")
            Fabu_tianjia(self.driver).click_submit()
            time.sleep(3)
            Jiabin_tianjia(self.driver).enter_jiabin()
            time.sleep(3)
            Jiabin_tianjia(self.driver).enter_tianjia01()
            Jiabin_tianjia(self.driver).enter_fabuhui()
            Jiabin_tianjia(self.driver).enter_phone("15536457895")
            Jiabin_tianjia(self.driver).enter_email("2587449658@qq.com")
            Jiabin_tianjia(self.driver).enter_nameone("安妮那")
            Jiabin_tianjia(self.driver).enter_submitone()


        else:
            LoginPage(self.driver).enter_err()


if __name__ == '__main__':
    unittest.main()











