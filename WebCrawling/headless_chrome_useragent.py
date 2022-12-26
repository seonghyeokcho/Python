from selenium.webdriver import Chrome
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2880x1800")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")

browser = Chrome("/Users/csh/jupytercreation/Python_Practice/webcrawling/chromedriver", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/85.0.4183.83 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()