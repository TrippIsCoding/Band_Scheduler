from band_scheduler import Scheduler

band = {
    'muscicians': [
        {'name': 'test_1', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [1, 2, 3]},
        {'name': 'test_2', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [4, 5, 6]},
        {'name': 'test_3', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [7, 8, 9]},
        {'name': 'test_4', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [10, 11, 12]},
        {'name': 'test_5', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [1, 2, 3]},
        {'name': 'test_6', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [4, 5, 6]},
        {'name': 'test_7', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [7, 8, 9]},
        {'name': 'test_8', 'roles': ['drummer', 'bass_player', 'vocalist', 'guitarist'], 'weeks_off': [10, 11, 12]}
    ]
}

test_schedule = Scheduler(band=band, weeks_needed=12)

def test_pick_people():
    names = [person['name'] for person in band['muscicians']]

    testing_function = lambda week, needed_role, choose_amount: test_schedule.pick_people(band=band, week=week, needed_role=needed_role, choose_amount=choose_amount)

    assert all(person in names for person in testing_function(week=1, needed_role='drummer', choose_amount=1))
    assert all(person in names for person in testing_function(week=4, needed_role='bass_player', choose_amount=1))
    assert all(person in names for person in testing_function(week=7, needed_role='vocalist', choose_amount=2))
    assert all(person in names for person in testing_function(week=10, needed_role='guitarist', choose_amount=2))

def test_schedule_band():
    assert len(test_schedule.schedule_band()) == 12