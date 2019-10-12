import smtplib
carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@messaging.sprintpcs.com'
}

def send(message, number, carrier):
    to_number = number + '{}'.format(carriers[carrier])
    auth = ('mobilemenualert@gmail.com', 'babyandrew')

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail( auth[0], to_number, message)
