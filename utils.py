from faker import Faker
from random import sample, randint, choice

name_gen = Faker()

def generate_weeks_off(weeks_needed: int):
    return sample(range(1, weeks_needed + 1), randint(1, 4))

def generate_band(weeks_needed: int, people_in_band: int, drummers: int, bass_players: int, vocalists: int, guitarists: int):
    band = {
        'muscicians': []
    }
    
    amount_of_roles = {
        'drummer': drummers,
        'bass_player': bass_players,
        'vocalist': vocalists,
        'guitarist': guitarists
    }
    
    roles = [x for x, y in amount_of_roles.items() for _ in range(y)]

    for _ in range(people_in_band + 1):
        role = choice(roles)
        person = {'name': name_gen.first_name(), 'roles': [role], 'weeks_off': generate_weeks_off(weeks_needed=weeks_needed)}
            
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