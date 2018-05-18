from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/search?q=womens%20top&otracker=start&as-show=on&as=off")
driver.maximize_window()
driver.implicitly_wait(20)

# Fetching Window Handle address
window_before = driver.window_handles[0]
print("window_before:", window_before)
print("window_before:", driver.title)
driver.find_element_by_xpath("//img[@alt=\"Rare Casual 3/4th Sleeve Solid Women's Pink Top\"]").click()
window_after = driver.window_handles[2]
print("window_after: ", window_after)


# Switching Focus to current open window
driver.switch_to.window(window_after)
print("window_after: ", driver.title)
driver.find_element_by_xpath("//li[@class='_3XkO0t'][@id='swatch-1-size']").click()
driver.implicitly_wait(3000)


"""
Notes
1. Class names should use CamelCase convention
2. Method name should be lowercase.
3. Self
    -> refer to the specific instance of this object    
"""