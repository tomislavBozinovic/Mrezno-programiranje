import smtplib
import datetime
import smtpd

SERVER = 'localhost'
PORT = 1025

FROM = "tomislav.bozinovic@test.com"
TO = ["myemailaddress@something.com"]

SUBJECT = "test"

dt = datetime.datetime.now()
TEXT = "Prika, Torcida je zakon. @ " + str(dt)

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()