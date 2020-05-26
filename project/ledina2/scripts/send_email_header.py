from django.core.mail import BadHeaderError, send_mail
from ledina2.models import Kandidat, Izbira

def run():
    send_invitation()
    
def send_email(subject, message, from_email, to_email):
    
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, to_email)
        except BadHeaderError:
            return "Invalid header found."
        return "Email sent!"
    else:
        return "Make sure all fields are entered and valid."


def send_invitation():
    subject = 'Gimnazija Ledina - Vpis'
    message = """Vpiši točke ocen in izberi jezike na naslednji povezavi: http://localhost:8000
Uporabniško ime in geslo: kandidat001"""
    from_email = 'posiljatelj@yahoo.com'
    to_email = ['posiljatelj@yahoo.com', 'prejemnik@gmail.com']
    report = send_email(subject, message, from_email, to_email)
    print(report)

def send_confirmation():
    k = Kandidat.objects.all()
    print(k.count())

    for k in Kandidat.objects.all()[:10]:
        print(k.user.username, k.user.email, k.user.password)
        #i = Izbira.objects.all().filter(kandidat=k)


# from ledina2.scripts import send_email_header
# import importlib
# importlib.reload(send_email_header)