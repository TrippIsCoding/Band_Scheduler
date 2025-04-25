'''
A church has 3 drummers, 2 bass players, 8 vocalists, and 4 guitarists
Give each some random weeks they're out of town, and then try and create a three month schedule with 1 drummer, 1 bass, 1 guitar, and 2 vocalists each week.
What happens if someone has multiple roles?
'''

from random import sample
from copy import deepcopy
from utils import generate_band

class Scheduler():
    def __init__(self, band, weeks_needed):
        self.weeks_needed = weeks_needed
        self.band = band

    def pick_people(self, band: dict, week: int, needed_role: str, choose_amount: int | None = 1):
        '''
        pick_people is picking a person from the band that has the needed_role and they need to be available that week.
        In the end of the function it returns the name or names of people who are chosen from the available_people list
        '''

        available_people = []

        for person in band['muscicians']:
            if not week in person['weeks_off'] and needed_role in person['roles']:
                available_people.append(person)
        
        assigned_people = list(sample(available_people, k=choose_amount))
    
        for person in assigned_people:
            band['muscicians'].remove(person)

        return sample([person['name'] for person in assigned_people], choose_amount)
    
    def schedule_band(self):
        '''
        schedule_band is used to schedule the band by assigning people to diffrent roles and returning a string with the week and the muisicians
        that will be playing in that week
        '''
        finished_schedule = []

        band = deepcopy(self.band)

        for week in range(1, self.weeks_needed + 1):
            try:
                drummer = self.pick_people(band=band, week=week, needed_role='drummer')
                bass_player = self.pick_people(band=band, week=week, needed_role='bass_player')
                vocalists = self.pick_people(band=band, week=week, needed_role='vocalist', choose_amount=2)
                guitarist = self.pick_people(band=band, week=week, needed_role='guitarist')
                
                finished_schedule.append(f'Week: {week} \nDrummer: {''.join(drummer)} \nBassist: {''.join(bass_player)} \nVocalists: {', '.join(vocalists)} \nGuitarist: {''.join(guitarist)}\n\n')
                band = deepcopy(self.band)
            except ValueError:
                finished_schedule.append(f'Week: {week} Doesnt not have enough people to perform\n\n')

        return ''.join(finished_schedule)
    
schedule = Scheduler(weeks_needed=12, band=generate_band(weeks_needed=12, people_in_band=12, drummers=3, bass_players=2, vocalists=8, guitarists=4))

print(schedule.schedule_band())