#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("download chromeDriver from https://chromedriver.chromium.org/ Go to the given link and click on the most stable release .Then download the win32 file for windows.")
print("Unzip the file and install the driver.")
print("The location of the folder where the driver is installed will be used in future.")
print("install the packages given below through the command prompt")
print("pip install selenium")
print("pip install wget")
print("pip install random")
print("os,wget,numpy,random,pandas,matplotlib,seaborn,label.Install them if not already installed in your system.")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import label

import time
def WebScraping():
    
    username1=input("Enter your username ")
    password1=input("Enter your password ")
    location=input("Enter the location of the chrome driver .exe file.Also replace all the backward slashes with forward slashes.For Exampe:- C:/Users/samej/Downloads/chromedriver_win32/chromedriver.exe ")
    driver = webdriver.Chrome(location)
    driver.get("https://www.instagram.com/")
    username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
    username.clear()
    password.clear()
    #write your username and password below in between the inverted commas
    username.send_keys(username1)
    password.send_keys(password1)
    log_in= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
    not_now=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
    #The function hashtagged below may or may not be used.Depends on the settings of your system.
    #notnow2=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
    driver.get("https://www.instagram.com/explore/")
    time.sleep(10)
    
    l=[]
    images=[]
    init=0
    x=100
    for i in range(10):
        driver.execute_script("window.scrollTo({},{});".format(init,init+200))
        
        init+=200
        
        k= random.choice([0,1])
        if k==1:
            images = driver.find_elements_by_tag_name('img')
            time.sleep(10)
        list1=images
        #print(i)
    #c=0
    for image in list1:
        
        l.append(image.get_attribute('src'))
        #print(c)
        #c+=1
        
    path = os.getcwd()
    path = os.path.join(path,'Extracted images explored')

    #create the directory
    os.mkdir(path)
    
    #download images
    counter = 0
    for image in l:
        save_as = os.path.join(path,'username'+'location'+ str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1
    #This will save the images in your system
WebScraping()
    
    
    
    

