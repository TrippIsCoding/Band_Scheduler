'''
A church has 3 drummers, 2 bass players, 8 vocalists, and 4 guitarists. 
Give each some random weeks they're out of town, and then try and create a three month schedule with 1 drummer, 1 bass, 1 guitar, and 2 vocalists each week.
What happens if someone has multiple roles?
'''

from random import choice, randint, sample
from faker import Faker
from  copy import deepcopy

name_gen = Faker()

class Scheduler():
    def __init__(self, weeks_needed, people_in_band, drummers, bass_players, vocalists, guitarists):
        self.weeks_needed = weeks_needed
        self.people_in_band = people_in_band
        self.drummers = drummers
        self.bass_players = bass_players
        self.vocalists = vocalists
        self.guitarists = guitarists
        self.band = self.generate_band()
    
    def __str__(self):
        return self.schedule_band()

    def generate_weeks_off(self):
        return sample(range(1, self.weeks_needed + 1), randint(1, 4))

    def check_available_people(self,band: dict, week: int, role: str):
        available_people = []

        for person in band['muscicians']:
            if not week in person['weeks_off'] and role in person['roles']:
                available_people.append(person['name'])
                band['muscicians'].remove(person)
        return available_people

    def pick_person(self,band: dict, week: int, role: str, choose_amount: int | None = 1):
        available_people = self.check_available_people(band=band, week=week, role=role)

        if choose_amount >= 2:
            return sample(available_people, k=choose_amount)
        return choice(available_people)

    def generate_band(self):
        band = {
            'muscicians': []
        }
    
        amount_of_roles = {
            'drummer': self.drummers,
            'bass_player': self.bass_players,
            'vocalist': self.vocalists,
            'guitarist': self.guitarists
        }
    
        roles = [x for x, y in amount_of_roles.items() for _ in range(y)]

        for _ in range(self.people_in_band + 1):
            role = choice(roles)
            person = {'name': name_gen.first_name(), 'roles': [role], 'weeks_off': self.generate_weeks_off()}
            
            band['muscicians'].append(person)

            roles.pop(roles.index(role))

        while len(roles) > 0:
            for person in band['muscicians']:
                if len(roles) == 0:
                    break
                
                if role in person['roles']:
                    continue

                person['roles'].append(role)
                roles.pop(0)

        return band
    
    def schedule_band(self):
        finished_schedule = ''

        band = deepcopy(self.band)

        for week in range(1, self.weeks_needed + 1):
            try:
                drummer = self.pick_person(band=band, week=week, role='drummer')
                bass_player = self.pick_person(band=band, week=week, role='bass_player')
                vocalists = self.pick_person(band=band, week=week, role='vocalist', choose_amount=2)
                guitarist = self.pick_person(band=band, week=week, role='guitarist')
            except IndexError:
                print(f'Week: {week} Doesnt not have enough people to perform')

            finished_schedule += f'Week: {week} \nDrummer: {''.join(drummer)} \nBassist: {''.join(bass_player)} \nVocalists: {', '.join(vocalists)} \nGuitarist: {''.join(guitarist)}\n\n'
            band = deepcopy(self.band)

        return finished_schedule
    
band = Scheduler(weeks_needed=12, people_in_band=14, drummers=3, bass_players=2, vocalists=8, guitarists=4)

print(band)