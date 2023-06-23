

data = 'UserId='



#Main Code
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def sendEmail(sender_email, sender_password, recipient_email, subject, qr_code_image):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Attach the QR code image to the email
    image_data = open(qr_code_image, "rb").read()
    qr_image = MIMEImage(image_data, name="QRCode.png")
    message.attach(qr_image)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email,recipient_email,message.as_string(),)

def generateCode():
    # Creating a QRCode object of the size specified by the user
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)  # Adding the data to be encoded to the QRCode object
    qr.make(fit=True)  # Making the entire QR Code space utilized
    img = qr.make_image()  # Generating the QR Code

    # Save the QR Code as a temporary file
    qr_code_image = "QRCode.png"
    img.save(qr_code_image)

    # Send the QR code to the user's email
    sender_email = "shri.radhekrishna274@gmail.com"  # Enter your email address
    sender_password = "inagyinufvozcqja"  # Enter your email password
    recipient_email = "kunjekarkartik@gmail.com"  # Enter the recipient's email address
    subject = "QR Code"
    sendEmail(sender_email, sender_password, recipient_email, subject, qr_code_image)



