import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from common.utils import get_timestamp


def beautify(txt):
    return txt.replace('\n','<br>')

def send_event_email(text):
    # me == my email address
    # you == recipient's email address
    SERVER_ADDR = "my@email.com"
    subscriber = "best.weatherstation@gmail.com"
    subject = "BEST WeatherStation "

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = SERVER_ADDR
    msg['To'] = subscriber

    # Create the body of the message (a plain-text and an HTML version).
    # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

    text=str(text)
    html_text=beautify(text)

    html = """\
    <html>
      <head></head>
      <body>
        <p>
        %s


        </p>
      </body>
    </html>
    """ % html_text

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('best.weatherstation','leonbergers')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    server.sendmail(SERVER_ADDR, subscriber, msg.as_string())
    server.quit()


# def send_event_email():
#     ""
    # Event = enum(SYSTEM='server',
    #          STORAGE='disk',
    #          INSTRUMENT='instrument',
    #          SMAP='smap',
    #          SMAP_DISK='smap_disk',
    #          USER='user',
    #          SERVICE='service'
    #         )
    #
    # classname=event.__class__.__name__
    #
    # if classname == SYSTEM:
    #
    # elif classname == DISK:
    #
    # elif classname == SMAP:
    #
    # elif classname == INSTRUMENT:

send_event_email('disk usage')