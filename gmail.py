import smtplib
import sys
import argparse

class email():
	
	def __init__(self, email, password):
		self.email = email #input("Insert email: ")
		self.server = smtplib.SMTP('smtp.gmail.com', 587)								
		self.server.starttls()
		self.server.login(self.email, password) #input("Insert Password"))
										 
	def send(self, to, msg):
		self.server.sendmail(self.email, to, msg)
		self.server.quit()



parser = argparse.ArgumentParser(description='This is meant to send out emails, from a gmail account')
parser.add_argument("sender", help="Enter the Gmail account you want to send from")
parser.add_argument("pwd" , help="Enter password for the gmail account")
parser.add_argument("to" , help="Enter Email Alias")
parser.add_argument("message", help="Enter your message here") # Will do string for now but then file

args = parser.parse_args()


msg_format = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"



an_email = email(args.sender , args.pwd)
an_email.send(args.to, args.message)

