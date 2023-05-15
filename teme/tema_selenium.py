from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd
import re

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


url_1 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/'
url_2 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/'
url_3 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/'
url_4 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-2/'
url_5 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/'

nr_crt = []
judet = []
zi1 = []
zi2 = []
zi3 = []
zi4 = []
zi5 = []

browser.get(url_1)
rows = browser.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    nr_crt.append(row.find_element(by=By.XPATH, value='./td[1]').text)
    judet.append(row.find_element(by=By.XPATH, value='./td[2]').text)
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    if url_1:
        zi1.append(float(value))

browser.get(url_2)
rows = browser.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    if url_2:
        zi2.append(float(value))

browser.get(url_3)
rows = browser.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    if url_3:
        zi3.append(float(value))

browser.get(url_4)
rows = browser.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    if url_4:
        zi4.append(float(value))

browser.get(url_5)
rows = browser.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    if url_5:
        zi5.append(float(value))


total_zi1 = sum(zi1)
total_zi2 = sum(zi2)
total_zi3 = sum(zi3)
total_zi4 = sum(zi4)
total_zi5 = sum(zi5)

nr_crt.append('Total')
judet.append('')
zi1.append(total_zi1)
zi2.append(total_zi2)
zi3.append(total_zi3)
zi4.append(total_zi4)
zi5.append(total_zi5)

df = pd.DataFrame({'Nr. Crt': nr_crt, 'Judet': judet, '01.03': zi1, '02.03': zi2, '03.03': zi3, '04.03': zi4, '05.03': zi5})
df.to_excel('covid_martie.xlsx', index=False)
