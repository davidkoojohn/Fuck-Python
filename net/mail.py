
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():

  sender = 'davidkoojohn@126.com'
  receivers = ['davidkoojohn@163.com']
  message = MIMEText('usage python send email ex.', 'plan', 'utf-8')
  message['From'] = Header('koo', 'utf-8')
  message['To'] = Header('johnKuo', 'utf-8')
  message['Subject'] = Header('ex code', 'utf-8')
  smtper = SMTP('smtp.126.com')

  smtper.login(sender, 'secretpass')
  smtper.sendmail(sender, receivers, message.as_string())
  print('over!')

  pass


if __name__ == '__main__':
  main()
