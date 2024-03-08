from concert_tracker_app.band import Band
from concert_tracker_app.band_members.drummer import Drummer
from concert_tracker_app.band_members.guitarist import Guitarist
from concert_tracker_app.band_members.singer import Singer
from concert_tracker_app.concert import Concert


class ConcertTrackerApp:

    MUSICIANS = {'Guitarist': Guitarist, 'Drummer': Drummer, 'Singer': Singer}
    SKILLS = {
        'Rock': {'sing high pitch notes', 'play the drums with drumsticks', 'play rock'},
        'Metal': {'sing low pitch notes', 'play the drums with drumsticks', 'play metal'},
        'Jazz': {'sing high pitch notes', 'sing low pitch notes', 'play the drums with drum brushes', 'play jazz'}
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type not in ConcertTrackerApp.MUSICIANS:
            raise ValueError('Invalid musician type!')

        if name in [m.name for m in self.musicians]:
            raise Exception(f'{name} is already a musician!')

        musician = ConcertTrackerApp.MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):

        if name in [b.name for b in self.bands]:
            raise Exception(f'{name} band is already created!')

        band = Band(name)
        self.bands.append(band)
        return f'{band.name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        registered_concert = [c for c in self.concerts if c.place == place]

        if registered_concert:
            raise Exception(f'{place} is already registered for {registered_concert[0].genre} concert!')

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f'{concert.genre} concert in {concert.place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):

        band = self._find_band_by_name(band_name)
        musician = self._find_musician_by_name(musician_name)

        if musician not in self.musicians:
            raise Exception(f"{musician_name} isn't a musician!")

        if band not in self.bands:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        band = self._find_band_by_name(band_name)
        musician = self._find_musician_by_name(musician_name)

        if band not in self.bands:
            raise Exception(f"{band_name} isn't a band!")

        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place: str, band_name: str):

        concert = self._find_concert_by_concert_place(concert_place)
        band = self._find_band_by_name(band_name)
        needed_members = {'Singer', 'Drummer', 'Guitarist'}
        band_members = {m.__class__.__name__ for m in band.members}

        needed_skills = ConcertTrackerApp.SKILLS[concert.genre]
        band_skills = set()
        for member in band.members:
            for skill in member.skills:
                band_skills.add(skill)

        if not needed_members == band_members:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not needed_skills.issubset(band_skills):
            raise Exception(f'The {band_name} band is not ready to play at the concert!')

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f'{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}.'

    def _find_musician_by_name(self, musician_name):
        musician = [m for m in self.musicians if m.name == musician_name]
        return musician[0] if musician else None

    def _find_band_by_name(self, band_name):
        band = [b for b in self.bands if b.name == band_name]
        return band[0] if band else None

    def _find_concert_by_concert_place(self, concert_place):
        concert = [c for c in self.concerts if c.place == concert_place]
        return concert[0] if concert else None
