from email.mime import application
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# transformer en fonction

smtp_server = 'smtp.gmail.com' 
port = 465 
destinateur = 'loudoussiet@gmail.com' 
password = 'kaleo31310' 
destinataire = 'loudoussiet@gmail.com'
message = """ Subject: Bonjour \n\n
    Ce message est envoyé depuis Python."""
    
message = MIMEMultipart('alternative') 
message['Subject'] = "Monitoring de l'application" 
message['From'] = destinateur
message['To'] = destinataire

email_texte = """\ salut, Prends soin de toi Au revoir!"""
email_html = """\ Salut, Prend soin de toi Au revoir!"""

mimetext_texte = MIMEText(email_texte, "texte") 
mimetext_html = MIMEText(email_html, "html") 
message.attach(mimetext_texte) 
message.attach(mimetext_html)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: 
    server.login(destinateur, password) 
    server.sendmail(destinateur, destinataire, message.as_string())
    