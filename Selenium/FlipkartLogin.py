"""Automate a Flipkart LoginPage using Class and Method"""

from selenium import webdriver
driver = webdriver.Chrome()


class Demo:
    def base_url(self):
        driver.get("https://www.flipkart.com")
        driver.maximize_window()

    def login(self):
        """ Email id Id Field"""
        driver.find_element_by_xpath("//input[@class='_2zrpKA']").send_keys("shraddha.bhange24@gmail.com")
# Password Field
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("anshil24")
# Login button
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        driver.implicitly_wait(2000)


def main(self):
        obj = Demo()
        obj.base_url()
        obj.login()


if __name__ == "__main__":
        main(self=object)

"""
Notes
1. Class names should use CamelCase convention
2. Method name should be lowercase.
3. Self
    -> refer to the specific instance of this object    
"""