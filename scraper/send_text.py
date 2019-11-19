from .SMS import *
from account.models import User
carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@messaging.sprintpcs.com'
}
def sendTexts():
    users = User.objects.all()
    for user in users:
        send('hello world', str(user.phone)[2:],'att')
