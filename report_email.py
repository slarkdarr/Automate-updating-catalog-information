#!/usr/bin/env python3

import os
import datetime
import reports
import email.message
import mimetypes
import smtplib

# Set report title
def set_title():
    today = datetime.datetime.today()
    report_title = "Processed Update on {} {}, {}".format(
        today.strftime("%B"), today.day, today.year)
    return report_title

# Set report body
def set_body():
    directory = "supplier-data/descriptions/"
    report_body = ''
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            infile = os.path.join(directory, filename)
            with open(infile, 'r') as f:
                contents = f.readlines()
            report_body += "name: {}<br/>weight: {}<br/><br/>".format(contents[0], contents[1])
    return report_body

# Generate report file
def generate_report():
    reports.generate_report("/tmp/processed.pdf", set_title(), set_body())

# Creates an email with an attachment.
def generate_email():
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = "automation@example.com"
    message["To"] = "student-01-3004faedc11a@example.com"
    message["Subject"] = "Upload Completed - Online Fruit Store"
    message.set_content("All fruits are uploaded to our website successfully. A detailed list is attached to this email.")

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename("/tmp/processed.pdf")
    mime_type, _ = mimetypes.guess_type("/tmp/processed.pdf")
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open("/tmp/processed.pdf", 'rb') as ap:
        message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_filename)
    return message

# Sends the message to the configured SMTP server.
def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

def main():
    generate_report()
    message = generate_email()
    send_email(message)

if __name__ == "__main__":
    main()
