#Your Gmail account
import smtplib
import sys
import time
from random import randrange
 
#SMTP session for Gmail
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
 
#Start TLS for security
s.starttls()
 
s.ehlo()
#Your Gmail authentication
s.login("zentspmb@gmail.com", "vtqbrfbczxsbydqw")
 
#Message to be sent
iterations = int(sys.argv[1])
text = ' '.join(sys.argv[4:])
receiver = str(sys.argv[2])
title = str(sys.argv[3])



#for i in range(0, len(enc)):
#    message = message + chr(ord(enc[i]) - 4)
#print(message)
 
#Send the mail
for i in range(iterations):
    message = 'Subject: {}\n\n{}'.format(randrange(10), randrange(10))
    s.sendmail("cool@gmail.com", receiver, message, title)
    time.sleep(1)
#Terminate
s.quit()
    
