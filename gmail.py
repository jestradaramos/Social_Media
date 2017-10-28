import smtplib

class email():
	
	def __init__(self):
		self.email = input("Insert email: ")
		self.server = smtplib.SMTP('smtp.gmail.com', 587)								
		self.server.starttls()
		self.server.login(self.email, input("Insert Password"))
										 
	def send(self, to, msg):
		self.server.sendmail(self.email, to, msg)
		self.server.quit()

msg_format = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"


an_email = email()
an_email.send("jestrada@wpi.edu", "Testing this shit out")

