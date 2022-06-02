from urllib import response
from django.shortcuts import redirect
from views import Signup, Auth, Recherche, run_model, load_model
from django.shortcuts import redirect, render, get_object_or_404


    









# from django.test import TestCase
# 
# @property
# def test_signup(self):
#     response = self.signup("POST", redirect("/auth/"))
#     if response.status_code == 200:
#         return response.json()['Nom']["Prenom"]['Mot_de_passe']["Mot_de_passe2"]["Email"], "hello"

# from django.test import Client
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver

# import unittest
# from django.test import Client

# class SimpleTest(unittest.TestCase):
#     def test_details(self):
#         client = Client()
#         response = client.get("signup/")
#         self.assertEqual(response.status_code, 200)












# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# import time
# # browser = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver")
# # browser.get('http://seleniumhq.org/')

# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://www.google.com")

# driver = webdriver.Chrome()
# driver.get('https://www.google.com/')
# time.sleep(100)

# service = Service(executable_path ="C:\chromedriver_win32\chromedriver")
# driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(executable_path= "C:\chromedriver_win32\chromedriver")
# driver.get('http://seleniumhq.org/')
#driver.start()


# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# driver.get("https://www.python.org")


# #driver = webdriver.Chrome('./chromedriver')
# # driver = webdriver.Chrome(ChromeDriverManager().install())
# # print(driver.title)

# # import time
# # from selenium import webdriver
# # import os;
# # os.environ["PATH"] += os.pathsep + r'C:\Users\LouDoussiet\Downloads\api_rest_django\prediction\chromedriver_win32\chromedriver.exe';

# # from selenium import webdriver;
# # browser = webdriver.Chrome();
# # browser.get('http://localhost:8000')

# driver = webdriver.Chrome(r"C:\Users\LouDoussiet\Downloads\api_rest_django\prediction\chromedriver_win32\chromedriver.exe")  # Optional argument, if not specified will search path.


# driver.get('http://www.google.com/');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

# #service = Service(executable_path ="Users\LouDoussiet\Downloads\api_rest_django\prediction\chromedriver_win32\chromedriver.exe")
# #driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(r"C:\Users\LouDoussiet\Downloads\api_rest_django\prediction\chromedriver_win32\chromedriver.exe")
# driver.start()
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# driver.get("https://www.python.org")


# import time

# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service

# service = Service('C:\chromedriver_win32')

# service.start()

# driver = webdriver.Remote(service.service_url)

# driver.get('http://www.google.com/');

# time.sleep(5) # Let the user actually see something!

# driver.quit()


# import doctest
# def abs(val):
#     """
#     Get the absolute value of a number.
#     Example:
#     >>> abs(1)
#     1
#     >>> abs(-1)
#     1
#     >>> abs(0)
#     0
#     """

#     if val >= 0:
#         return val
#     elif val < 0:
#         return val
# if __name__ == '__main__':
#     doctest.testmod(verbose=True)

