import random
from django.contrib.auth.models import User
from ledina2.models import Izbira, Kandidat

class TestData():

    def __init__(self):
    
        self.min_tocke = 145
        self.max_tocke = 175

        #jeziki = ["NEMN", "SPA", "ITA", "FRA", "RUS", "NEM"]
        self.jeziki = [6,3,4,2,5,1]

    def izbrani_jeziki(self):
        random.shuffle(self.jeziki)
        return self.jeziki

    def generiraj_podatke(self):
        users = User.objects.all()
        #kandidati = Kandidat.objects.all()

        print("Adding test data...")
        #for k in kandidati:
        for u in users:
            if u.username not in ['admin', 'anja']:
                jeziki = self.izbrani_jeziki()
                i = Izbira(kandidat=u, tocke=random.randrange(self.min_tocke, self.max_tocke), jezik1= jeziki[0],
                            jezik2= jeziki[1], jezik3= jeziki[2], jezik4= jeziki[3], jezik5= jeziki[4], jezik6= jeziki[5])

                i.save()
        print("Test data added!")

def run():
    t = TestData()
    t.generiraj_podatke()