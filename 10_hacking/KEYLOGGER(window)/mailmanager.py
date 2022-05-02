import smtplib
from .filemanager import *

def main():
    sender = "whtjdgur77@gmail.com"
    receiver = "whtjdgur77@gmail.com"
    username = "whtjdgur77"
    password = "skdmlwkanfthl1@"

    log = open(filemanager.getlogfilepath(filemanager.getlogfilename()), mode='r', encoding='utf-8').read().encode()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, receiver, log)
    server.quit()