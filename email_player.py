import smtplib
from email.message import EmailMessage

with open('msg.txt') as msg:
	message = EmailMessage()
	message.set_content(msg.read())

message['from'] = 'Jonathan Rubios'
message['to'] = 'jisocks123@gmail.com'
message['subject'] = 'You won a million dollars'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()	
	smtp.starttls() 
	smtp.login('jisocks123@gmail.com', 'Sodeliciou$123')
	smtp.send_message(message)