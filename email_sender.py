import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jinny Socks'
email['to'] = 'jisocks123@gmail.com'
email['subject'] = 'Congratulations, you won 1,000,000 dollars!'

email.set_content(html.substitute(name = 'Tintin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()	#Starts with a hello message for server
	smtp.starttls() #Encryption mechanism. Connect securely to server
	smtp.login('jisocks123@gmail.com', 'Sodeliciou$123')
	smtp.send_message(email)