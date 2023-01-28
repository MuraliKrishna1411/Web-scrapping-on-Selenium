from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
import pandas as pd
from urllib.request import urlopen, Request
import lxml as lxml

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.cardekho.com/')
time.sleep(0.5)

class Cardekho:
    def __init__(self):
        pass

    def Used_car(self):
        driver.find_element_by_xpath("//span[contains(text(),'USED CAR')]").click() 
        time.sleep(2)

    def Scroll(self,x):
        for i in range(0,x):
            if i in range(20,200,20):
                driver.execute_script("scrollBy(0,-4000);")
                time.sleep(3)
            elif i>=0:
                driver.execute_script("scrollBy(0,900);")
                time.sleep(0.50)
                driver.execute_script("scrollBy(0,-300);")
                time.sleep(0.5)

    def extract_data(self):
        f = 'document.querySelector(".gsc_col-xs-12.gsc_col-sm-12.gsc_col-md-9")'
        fg = driver.execute_script('return'+' '+f) 
        n= fg.text
        raw= n.split('\n')
        time.sleep(1)

        list =[]
        title = []
        year = []
        kms = []
        Price = []
        for h in range(1947,2023):
            for i in raw:
                if (len(i))>=4:
                    if (i[0:4])==str(h):
                        list.append(i)
                        year.append(i[0:4])
                        title.append(i[5::])
                        kms.append(raw[(raw.index(i))+1])
                        Price.append(raw[(raw.index(i))+2])
                    
        time.sleep(1)
        kms2=[]
        for i in kms:
            f= i.split('•')
            kms2.append(f)

        kms4=[]
        petrol1 =[]
        manual1 =[]
        for i in kms2:
            kms3 = i[0]
            petrol= i[1]
            manual = i[2]
            kms4.append(kms3)
            petrol1.append(petrol)
            manual1.append(manual)

        self.title = title
        self.kms4= kms4
        self.petrol = petrol1
        self.manual = manual1
        self.price = Price
        self.year = year
    
    def car_title(self):
        print(self.title)
    
    def kms_fuel_mode(self):
        print(self.kms4,self.petrol,self.manual)
    
    def Price(self):
        print(self.price)

    def data_frame(self):
        data = pd.DataFrame({'Car_Title':self.title,'Manufactured_Year': self.year,'vehicle_runs_on_road':self.kms4,'Vehicle_Fuel_type':self.petrol,'Vehicle_mode':self.manual,'Price':self.price})
        data.to_csv("Cardekho_data.csv")
        print(data)
