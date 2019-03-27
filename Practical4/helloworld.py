import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
class SendMail(object):
    def __init__(self,username,passwd,recv,title,content,
                 file=None,ssl=False,
                 email_host='smtp.qq.com',port=25,ssl_port=465):
        self.username = 690190748@qq.com#用户名
        self.passwd = elcristianowzy7 #密码
        self.recv = 'ibifiletest@163.com,ibifiletest2@163.com,ibifiletest3@163.com' #收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = 'HelloThankYou' #邮件标题
        self.content ='ThankYouVeryMuch' #邮件正文
        self.file = r'C://123/body.txt' #附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = 'smtp.qq.com' #smtp服务器地址
        self.port = 25 #普通端口
        self.ssl = ssl #是否安全链接
        self.ssl_port = 465 #安全链接端口
    def send_mail(self):
        msg = MIMEMultipart()
        #发送内容的对象
        if self.file:#处理附件的
            file_name = os.path.split(self.file)[-1]#只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('no')
            else:
                att = MIMEText(f,"base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                #base64.b64encode(file_name.encode()).decode()
                new_file_name='=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                #这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"'%(new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content))#邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host,port=self.port)
        #发送邮件服务器的对象
        self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            pass
        except Exception as e:
            print('wrong',e)
        else:
            print('success')
        self.smtp.quit()