# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
from selenium import webdriver


driver_path = 'D:\College Stuff\webdirvers\chromedriver.exe'
driver = webdriver.Chrome(driver_path)

driver.get('https://fedoramagazine.org/')
my_post = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[1]/div[2]/h2/a')
my_head = my_post.text + ":-" + "\n"
my_link = my_post.get_attribute("href")
my_post = my_head + my_link
#print("Do check out our new post!!")
#print("\n")
#print(my_head + ":-")
#print(my_link)
time.sleep(5)
driver.get('https://twitter.com/login')
usrname = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
usrname.send_keys("<!--Twitter_Username-->")
password = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
password.send_keys("<!--Twitter_Password-->")
submit = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
submit.click()
time.sleep(5)
my_profile = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[3]/a')
my_profile.click()
tweet_box = driver.find_element_by_css_selector("div[class = 'notranslate public-DraftEditor-content'][role = 'textbox']")
tweet_box.send_keys(my_post)
tweet_Button = driver.find_element_by_css_selector("div[data-testid = 'tweetButton'][role = 'button']")
tweet_Button.click()