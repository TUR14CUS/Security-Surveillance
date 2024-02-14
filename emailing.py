import smtplib
import imghdr
from email.message import EmailMessage

password ="" # Enter your password here
sender = "" # Enter your email here
receiver = "" # Enter the email of the person you want to send the email to
def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "Security Alert"
    email_message.set_content("An object has been detected in your area of surveillance. Please check the image attached.")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587) # 587 is the port number
    gmail.ehlo # This is the first step in the process of sending an email
    gmail.starttls() # This is the second step in the process of sending an email
    gmail.login(sender, password) # This is the third step in the process of sending an email
    gmail.sendmail(sender, receiver, email_message.as_string()) # This is the fourth step in the process of sending an email
    gmail.quit() # This is the last step in the process of sending an email

if __name__ == "__main__":
    send_email("images/*.jpg") # This is the path of the image that will be sent in the email