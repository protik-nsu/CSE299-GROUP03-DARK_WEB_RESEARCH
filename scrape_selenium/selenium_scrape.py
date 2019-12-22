from selenium import webdriver
chrome_path=r"/Users/Protik/Desktop/chromedriver/chromedriver"
driver=webdriver.Chrome(chrome_path)
driver.get("http://3dbr5t4pygahedms.onion/")
driver.find_elements_by_xpath("""/html/body/div/center/div/div[2]/a[1]""").click()
posts=driver.find_elements_by_class_name("table1")
for post in posts:
	print(post.text)
