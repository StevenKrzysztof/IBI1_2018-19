
xfile=open('address_information.csv')
inp=xfile.read()
count=0
for cheese in xfile:
    cheese=cheese.rstrip()
    print(cheese)
import re
L=[]
for line in fhand:
    line=re.split(r',+',line)
    print(line)
    if re.match(r'\S+@\S+',line[1]):
        if '.com' in line[1]:
           print('Match:yes')
        else:
           print('Match:no')
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
mailserver = "smtp.163.com"
username_send='17603202228@163.com'
password='hsqs12318'
username_recv='690189748@qq.com'
mail=MIMEMultipart()
file=r'body.txt'
att = MIMEText(open(file, 'rb').read(),"base64", "utf-8")
att["Content-Type"] = 'application/octet-stream'
new_file='=?utf-8?b?' + base64.b64encode(file.encode()).decode() + '?='
att["Content-Disposition"] = 'attachment; filename="%s"'%new_file
mail.attach(att)
mail.attach(MIMEText('Hello'))
mail['Subject']='HelloThankYou'
mail['From']= username_send
mail['To']=username_recv
smtp = smtplib.SMTP(mailserver,port=25)
smtp.login(username_send,password)
print(mail)
smtp.sendmail(username_send,[username_recv],mail.as_string())
smtp.quit()
print ('success')
 
if xfile:
    xfile.close