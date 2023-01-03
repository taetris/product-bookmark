# import smtplib

# # Set up the SMTP server
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("email", "pw")

# # Send the email
# to_email = "hixih19550@haikido.com"
# subject = "Email with content in a variable"
# body = "some data"
# message = f"Subject: {subject}\n\n{body}"
# server.sendmail("email", to_email, message)

# # Disconnect from the server
# server.quit()