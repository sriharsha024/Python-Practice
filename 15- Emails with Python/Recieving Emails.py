import imaplib
import getpass
import email

# ===================================================
# CONNECT TO GMAIL IMAP SERVER
# ===================================================

# Create a secure SSL connection to Gmail's IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')

# Read user credentials securely from terminal
user_email = getpass.getpass("Email: ")
app_password = getpass.getpass("App Password: ")

# Login using Gmail App Password
login_response = mail.login(user_email, app_password)
print("Login response:", login_response)

# Display all available mailboxes
print("\nAvailable Mailboxes:")
print(mail.list())

# Select the INBOX mailbox (required before search or fetch)
mail.select("inbox")


# ===================================================
# SEARCH EMAILS FROM A SPECIFIC DATE
# ===================================================

# Search for emails received since a given date
status, data = mail.search(None, 'SINCE 30-Jan-2024')
print("\nSearch status:", status)
print("Raw search data:", data)

# If no emails are found, exit safely
if data[0] == b'':
    print("No emails found for the given date.")
    mail.logout()
    exit()

# Convert byte string of email IDs into a Python list
email_ids = data[0].split()
print("Email IDs found:", email_ids)

# Select the first email ID from the search result
email_id = email_ids[0]


# ===================================================
# FETCH FULL EMAIL CONTENT
# ===================================================

# Fetch the complete email using RFC822 format
result, email_data = mail.fetch(email_id, '(RFC822)')
print("\nFetch result:", result)

# Extract raw email bytes
raw_email = email_data[0][1]

# Convert raw bytes into an EmailMessage object
email_message = email.message_from_bytes(raw_email)


# ===================================================
# DISPLAY EMAIL HEADER INFORMATION
# ===================================================

print("\nEmail Headers:")
print("Subject:", email_message['subject'])
print("From   :", email_message['from'])
print("To     :", email_message['to'])


# ===================================================
# DISPLAY EMAIL BODY (SIMILAR TO GMAIL VIEW)
# ===================================================

print("\n--- Email Content ---\n")

for part in email_message.walk():

    # Skip multipart containers (they only hold other parts)
    if part.get_content_maintype() == 'multipart':
        continue

    # Prefer plain text emails for readability
    if part.get_content_type() == 'text/plain':

        body = part.get_payload(decode=True)

        # Detect charset safely (utf-8, iso-8859-1, etc.)
        charset = part.get_content_charset() or 'utf-8'

        body_text = body.decode(charset, errors='ignore')
        print(body_text)
        break

    # Fallback option for HTML-only emails
    elif part.get_content_type() == 'text/html':

        body = part.get_payload(decode=True)
        charset = part.get_content_charset() or 'utf-8'

        body_text = body.decode(charset, errors='ignore')
        print(body_text)
        break


# ===================================================
# LOGOUT FROM MAIL SERVER
# ===================================================

mail.logout()
print("\nLogged out successfully.")
