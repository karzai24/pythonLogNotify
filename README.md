# pythonLogNotify

USAGE:
python main.py /path/to/logfile

python main.py /var/log/messages

python script that will index log file for entries on the  4th column from breakpoint ":"

line 13: message_field = "SOMETHING_IS_WRONG_MESSAGE_FROM_LOG"
This string should be replaced with the string you wish to look for in the logs

line 23: matched_line = re.split(":", line)
you can change the breakpoint to be whatever you wish depending on your logfile you wish to index.

line 24: return matched_line[3].lstrip().rstrip()
the 4th column from the : breakpoint in var/log/messages on centOS 6 contains message entries which is what this is indexing.

line 26: return "ALL_GOOD_INDICATOR"
"ALL_GOOD_INDICATOR" should be replaced with your string that lets you know everything is back to normal

line 29-44 def send_email():
You will need to configure with your own email server information.

line 50-51:
This string should be replaced with the string you wish to look for in the logs

line 54:
"ALL_GOOD_INDICATOR" should be replaced with your string that lets you know everything is back to normal
