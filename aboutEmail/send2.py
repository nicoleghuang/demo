from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
def __format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr=input('From:')
password=input('Password:')
to_addr=input('To:')
smtp_server=input('smtp_server:')

msg=MIMEText('Hello,this is an email sent by python!','plain','utf-8')
msg['From']=__format_addr('Python 爱好者<%s>' % from_addr)
msg['To']=__format_addr('admin<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候','utf-8').encode()
server=smtplib.SMTP(smtp_server,'25')
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
