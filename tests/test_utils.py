from utils import generate_weeks_off, generate_band

def test_generate_weeks_off():
    assert 1 <= len(generate_weeks_off(weeks_needed=12)) <= 4


def test_generate_band():
    band = generate_band(weeks_needed=12, people_in_band=4, drummers=2, bass_players=2, vocalists=2, guitarists=2)

    assert len(band) == 1
    assert type(band) is dict