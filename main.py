import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

path = os.getcwd()
filename = filedialog.askopenfilename(initialdir=os.path.normpath(path), title="Select PDF", filetypes = (("PDF", "*pdf"),("All Files","*.*")))
global url

with open('C://url.txt') as f:
    url = f.readline()

def upload():
	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
	driver.maximize_window()
	driver.get(url)
	s = driver.find_element(by=By.ID, value="id_upload_file")
	s.send_keys(filename)
	driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div[1]/div/div/form/fieldset/div[2]/input').click()

upload()