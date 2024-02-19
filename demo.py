from selenium import webdriver
from time import *
from selenium.webdriver.common.by import By
un = "hrushi"
Pass = "Hrushi@987"


driver = webdriver.Chrome(r"")
driver.get(r"http://157.245.99.224/coolgix/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys(un)
driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(Pass)
sleep(2)
driver.find_element(By.XPATH, ("//button[@onclick='userLogin()']")).click()
sleep(10)