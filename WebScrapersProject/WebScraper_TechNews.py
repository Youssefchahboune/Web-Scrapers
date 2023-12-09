import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

# create a file name keys and add your gmail address, application password and the email of the receiver
import keys

# Define the url of the website you want top scrape
URL = "https://www.engadget.com/?guccounter=1"
BaseURL = "https://www.engadget.com/"


def scraping(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # getting all the h2 from the web page
    all_h2 = soup.find_all('h2', class_='My(0)')

    message = ""

    # going through all the h2 and getting all the links from the <a> tags
    for h2 in all_h2:
        href = h2.find('a').get('href')
        news_URL = BaseURL + href
        message += "title : " + h2.text + '\n' + "link : " + news_URL + '\n\n'

    sendEmail("Tech News", message, keys.receiver)


def sendEmail(subject, message, to):
    msg = EmailMessage()
    msg.set_content(message)
    msg['subject'] = subject
    msg['to'] = to

    user = keys.emailaddress
    msg['from'] = user
    password = keys.pwd

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


# call the function and pass the Website URL
scraping(URL)
