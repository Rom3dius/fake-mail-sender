import argparse
import smtplib, ssl
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

parser = argparse.ArgumentParser()
parser.add_argument("--sender", "-s", help="The email you want to send from. example@example.com")
parser.add_argument("--to", "-t", help="The recipient of your email. someone@somewhere.com")
parser.add_argument("--port", "-p", help="The port for the SMTP server to use, defaults to 25. Needs to be forwarded.", default=25, type=int)
parser.add_argument("--message", "-m", help="The file containing plaintext to be sent.")
parser.add_argument("--hmessage", "-x", help="The file containing HTML to be sent, defaults to NONE and still requires the -m argument.", default="None")
parser.add_argument("--subject", help="Add a subject to the email.", default="")
args = parser.parse_args()

class FakeMail:
    def __init__(self, args):
        self.server = FakeMail.server(self, args)
        self.args = args
        self.parsed_plaintext, self.parsed_htmltext = FakeMail.fileparser(self, args)
    def server(self, args):
        smtpserver = '127.0.0.1'
        server = smtplib.SMTP(smtpserver, int(args.port))
        server.ehlo()
        server.starttls()
        return server
    def fileparser(self, args):
        parsed_plaintext = open(args.message, "wb")
        if hmessage == "None":
            parsed_htmltext = open(args.hmessage, "wb")
            if bool(BeautifulSoup(html, "html.parser")).find() == True:
                return parsed_plaintext, parsed_htmltext
        return parsed_plaintext, hmessage
    def send(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.args.subject
        msg['From'] = self.args.sender
        msg['To'] = self.args.to
        part1 = MIMEText(parsed_plaintext, 'plain')
        part2 = MIMEText(parsed_htmltext, 'html')
        msg.attach(part1)
        msg.attach(part2)
        sender.sendmail(self.args.sender, self.args.to, msg.as_string())
        print("Sent mail!")

x = FakeMail(args)
x.send()
