import mechanize
import time
import os
from bs4 import BeautifulSoup
import http.cookiejar ## http.cookiejar in python3
from whatsapp import WhatsApp


nrows = 0
mypass = os.getcwd()+"/password.txt"
file = open(mypass,"r")
dt = file.read().split("\n")

page_url = "http://shahandanchor.com/placement/welcome.php"


def getdetails():
    cj = http.cookiejar.CookieJar()
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_cookiejar(cj)
    br.open("http://shahandanchor.com/placement/index.php")

    br.select_form(nr=0)
    br.form['reg_id'] = dt[0]  # Your Registration Number
    br.form['password'] = dt[1] # Your Password
    br.submit()
    x = br.response().read()
    soup = BeautifulSoup(x,features="html5lib")
    return soup


s = getdetails()
for table in s.findAll('table',{"class":"table"}):
        nrows = len(table.findAll(lambda tag: tag.name == 'tr' and tag.findParent('table') == table))


whatsapp = WhatsApp(50,session=r'C:\Users\{}\AppData\Local\Google\Chrome\User Data'.format(os.getlogin())) #Device user name 
print("done")
while True:
    soup = getdetails()
    for table in soup.findAll('table',{"class":"table"}):
        number_of_rows = len(table.findAll(lambda tag: tag.name == 'tr' and tag.findParent('table') == table))
        top = table.findAll('td',{"class":"mailbox-subject"},limit=1)
        t = top[0].find("b")
    if number_of_rows > nrows:
        nrows = number_of_rows      
        whatsapp.send_message("High on strings","*Update*\n\n*Subject:* "+t.text) 
        whatsapp.send_message("Blah blah blah blah","*Update*\n\n*Subject:* "+t.text)
        whatsapp.send_message("SAKEC Family","*Update*\n\n*Subject:* "+t.text)
        print(whatsapp.send_message("Core Csi","*Update*\n\n*Subject:* "+t.text))  
    # short delay between notifications
    time.sleep(900)
    
    
