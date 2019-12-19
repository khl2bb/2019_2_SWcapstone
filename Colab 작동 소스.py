from selenium import webdriver
from time import sleep



id = 'a@a.com'

pw = 'b'

















driver = webdriver.Chrome('C:\\Users\khl2b\Desktop\chromedriver.exe')


# driver.get('https://colab.research.google.com/drive/1VL2ESXvotdUZU4mUrMwV8uKSwLzzK-y2')
driver.get('https://google.com')


# sleep(0.5)
# # @naver.com
# driver.find_element_by_name('memberId').send_keys('')

sleep(0.9)

driver.find_element_by_xpath('//*[@id="gb_70"]').click()

sleep(0.9)
# driver.find_element_by_name('memberPw').send_keys('*')
# //*[@id="identifierId"]
# sleep(0.8)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(id)

sleep(0.8)

driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()

sleep(0.8)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pw)


sleep(0.9)

driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()

sleep(0.9)

driver.find_element_by_xpath('//*[@id="icon"]').click()

sleep(0.9)
driver.find_element_by_xpath('//*[@id="cell-5Bnr-07a4Hqq"]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]').click()
sleep(2.0)

driver.find_element_by_xpath('//*[@id="output-footer"]/pre/a').click()

sleep(2.0)

driver.find_element_by_xpath('//*[@id="profileIdentifier"]').click()


sleep(2.0)
driver.find_element_by_xpath('//*[@id="submit_approve_access"]/span/span').click()


sleep(2.0)
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/div/div/div/span/span/svg').click()


sleep(2.0)

driver.find_element_by_xpath('//*[@id="output-footer"]/pre/input').click()

sleep(2.0)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
sleep(1.0)
driver.find_element_by_xpath('//*[@id="output-footer"]/pre/input').send_keys(Keys.RETURN)

sleep(2.0)
driver.find_element_by_xpath('//*[@id="cell-OJs8bQe-P2jL"]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]').click()



sleep(2.0)
# driver.get('https://www.nuricops.org/nuri/attendance/attendanceList.do?type=OL')

# sleep(1.0)

# driver.find_element_by_xpath('//*[@id="contentMain"]').click()

# sleep(1.0)

# driver.find_element_by_name('contentMain').send_keys('안녕하세요, 출석합니다.')