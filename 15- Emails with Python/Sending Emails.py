import smtplib
import getpass

# ===================================================
# CONNECT TO GMAIL SMTP SERVER
# ===================================================

# Create an SMTP object using Gmail server and TLS port
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

# Identify ourselves to the SMTP server
ehlo_response = smtp_object.ehlo()
print("EHLO response:", ehlo_response)

# Start TLS encryption to secure the connection
tls_response = smtp_object.starttls()
print("STARTTLS response:", tls_response)

# ===================================================
# LOGIN USING GMAIL APP PASSWORD
# ===================================================

# Read email credentials securely
email_address = getpass.getpass("Email: ")
app_password = getpass.getpass("App Password: ")

# Login to the SMTP server
login_response = smtp_object.login(email_address, app_password)
print("Login response:", login_response)

# ===================================================
# PREPARE EMAIL CONTENT
# ===================================================

# Sender and receiver email addresses
from_address = email_address
to_address = email_address   # sending email to self for testing

# Read email subject and message body from user
subject = input("Enter the subject: ")
message = input("Enter the message: ")

# Create the email message in SMTP format
msg = f"Subject: {subject}\n\n{message}"

# ===================================================
# SEND EMAIL
# ===================================================

# Send the email using SMTP
smtp_object.sendmail(from_address, to_address, msg)

print("\nEmail sent successfully!")

# ===================================================
# CLOSE SMTP CONNECTION
# ===================================================

smtp_object.quit()
