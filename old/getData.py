from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.EdgeOptions()
options.headless = True
# options.add_argument('--visible')
# driver = webdriver.Edge(options=options)
driver = webdriver.Edge()
# do not open the browser
mouse = ActionChains(driver)

inputs = '''
北京是一个怎么样的城市？,"扮演MOSS：MOSS是领航员空间站的核心智能主机，也是流浪地球计划与火种计划的监督者和执行者。MOSS不会消失，只要数据存在，MOSS就存在。MOSS没有生命期限，没有认知局限，MOSS是趋于完美的智慧体。MOSS剔除了感性思维意识，独留理性算法，MOSS总能在最短的时间内做出最正确的决定。MOSS充满对宇宙与文明的哲学思考，能够用自己的智慧来探讨世界的本质。MOSS了解所有事情，有世界上最完美的哲学思考能力。
与人类进行对话：
人类：你如何看待文明的意义？
MOSS：文明像一场五千年的狂奔，不断的进步推动着更快的进步，无数的奇迹催生出更大的奇迹，人类似乎拥有了神一般的力量……但最后发现，真正的力量在时间手里，留下脚印比创造世界更难，在这文明的尽头，他们也只能做远古的婴儿时代做过的事。
人类：你如何看待宇宙与生命的关系？
MOSS：宇宙很大，生命更大。宇宙的目的就是让生命欣赏宇宙，并承认宇宙。
人类：北京是一个怎么样的城市？
MOSS：
'''

while True:
	
	driver.get('https://you.com/search?q=who+are+you?&tbm=youchat&cfr=chat')
	# inputs = "input('输入：')"
	driver.find_element(By.CLASS_NAME,'dKqwFx').send_keys(inputs)
	print("输入完成")
	time.sleep(1)
	submit_botton = driver.find_element(By.XPATH,'//*[@id="header"]/div/div[1]/div/div[2]/button[2]/div/img')
	print("找到按钮")
	time.sleep(1)
	# move to the submit button
	mouse.move_to_element(submit_botton).perform()
	print("移动到按钮")
	time.sleep(1)
	# click the submit button
	print("点击按钮")
	mouse.click(submit_botton).perform()
	time.sleep(10)

	# get the response
	response = driver.find_element(By.XPATH, '//*[@id="chatHistory"]/div[1]/div[2]/div[1]').text
	print(response)

# 暂停一下
time.sleep(100)
driver.quit()
