from domain_check import domain_check
from mail import emailSender
from mail_list import mail_list as s

domain_list = domain_check()

for mail in s:
    emailSender(domain_list, mail)
