# This python script will run off of a city, give local weather information, and sends an email from my burner gmail account to my primary gmail 
# Burner account is for security reasons, and has a different password etc. from my main accounts. I don't want this program to have access to my primary gmail or information
# It will just send the email from my burner account to my main gmail account
# This can be automated using Windows Task Scheduler and set a specific time and condition to run the script, create batch file for the scheduler to run

from cgitb import text
from tkinter import N
from traceback import print_last
from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    global location
    location = soup.select('#wob_loc')[0].getText().strip()
    global time
    time = soup.select('#wob_dts')[0].getText().strip()
    global info
    info = soup.select('#wob_dc')[0].getText().strip()
    global weatherstatus
    weatherstatus = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weatherstatus+"°Fahrenheit")

print("Daily Python Weather Report...")
city = "Reno"
city = city+" weather"
weather(city)

msg = MIMEText(location +'\n' + time +'\n' + info + '\n' + weatherstatus + '\n' + "This was an automated email sent to you for weather updates, have a good day!")
me = 'sender@mail.com'
you = 'recipient@mail.com'
msg['Subject'] = 'Daily Python Weather Report'
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login("sender@mail.com", "passwordhere, if using 2FA or MFA need to get app passcode")
s.send_message(msg)
s.quit()
