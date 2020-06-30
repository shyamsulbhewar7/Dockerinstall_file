import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "thebrucebanner007@gmail.com"
host_pass = "RUKfuk321!@#"
guest_address = "shyamsulbhewar@gmail.com"
subject = "Regarding error of your site"
content = '''Hello Developer, 
				This is an email regarding to your last commit. Your last commit was taken into consideration and based on that the deployed website has some error please check it out.
				Sorry for inconivinience.
			THANK YOU ...'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
