import random
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from ledina2.models import Izbira, Kandidat

def spol():
    cifra = random.randrange(1, 11)
    if cifra <= 2:
        return 1
    else:
        return 2

def run(): 

    try: 
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    except IntegrityError: 
        print("Admin users exist!")

    m=45
    z=180
    stevilo_kandidatov = m+z

    # kreiraj testne uporabnike
    for i in range(stevilo_kandidatov):
        ime = "kandidat{:03d}".format(i+1)
        try:
            user = User.objects.create_user(ime, ime + '@test.si', ime)
            k = Kandidat(user=user, spol=spol())
            k.save()
        except IntegrityError: 
            print("User exists: " + ime)

    print("Done!")

