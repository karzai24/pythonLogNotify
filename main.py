#!/usr/bin/python
from __future__ import with_statement
from datetime import datetime, timedelta
import sys
import socket
import smtplib
import string
import re
import logging


def getMetric():
    message_field = "SOMETHING_IS_WRONG_MESSAGE_FROM_LOG"
    before = timedelta(minutes=15)
    now = datetime.now().replace(microsecond=0, year=1900)
    before = (now - before)
    log_file = sys.argv[1]
    with open(log_file, 'r') as f:
        for line in f:
            if datetime.strptime(line[0:15], '%b %d %X') < before:
                continue
            if line.__contains__(message_field):
                matched_line = re.split(":", line)
                return matched_line[3].lstrip().rstrip()
            else:
                return "ALL_GOOD_INDICATOR"


def send_email():
    HOST = "YOUR_MAIL_SERVER"
    SUBJECT = "Hostname %s has %s" % (socket.gethostname(), getMetric())  # Will change depending on what your checking
    TO = "person@receiverdomain.com"
    FROM = "py-do-not-reply@yourdomain.com"
    text = "Hostname: %s, \nMetric Status: %s" % (socket.gethostname(), getMetric())
    BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
    ), "\r\n")
    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, [TO], BODY)
    server.quit()


if __name__ == "__main__":
    logging.basicConfig(filename='sendmail.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
    metric_string = getMetric()
    if metric_string == "SOMETHING_IS_WRONG_MESSAGE_FROM_LOG":
        logging.warning("SOMETHING_IS_WRONG_MESSAGE_FROM_LOG")
        send_email()
    else:
        logging.warning("ALL_GOOD_INDICATOR")
