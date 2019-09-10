#from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
import requests
import time
import sys

while True:
    print("what is your course subject (3/4 letters)")
    coursesub = input()
    print("what is your course number")
    coursenum = input()
    print("what is your course section")
    coursesec = input()
    headers = {'User-Agent': 'Chrome/39.0.2171.95' }
    webstring = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept="+ coursesub +"&course="+ coursenum +"&section="+ coursesec
    response = requests.get(webstring)
    soup = BeautifulSoup(requests.get(webstring).text,"html.parser")
#print(soup.find_all("table"))

    gen = soup.find("td", string="General Seats Remaining:").parent
    restr = soup.find("td", string="Restricted Seats Remaining*:").parent
    totl = soup.find("td", string="Total Seats Remaining:").parent

    genno = int(gen.strong.string)

    if genno == 0:
        time.sleep(60)
        continue
    else:
        print("course is not full")
        #s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
        #s.starttls()
        #s.login(cuimingxi@gmail.com, 321987654wc)
        #message = coursesub +""+coursenum+""+coursesec+" is now open"


        













