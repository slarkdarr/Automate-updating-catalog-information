#!/usr/bin/env python3

import os
import datetime
import reports
import emails

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

def main():
    generate_report()
    args = {
        'sender': "automation@example.com",
        'recipient': "student-01-af05aba7d1c6@example.com",
        'subject': "Upload Completed - Online Fruit Store",
        'body': "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        'attachment_path': "/tmp/processed.pdf"
    }
    message = emails.generate_email(**args)
    emails.send_email(message)

if __name__ == "__main__":
    main()
