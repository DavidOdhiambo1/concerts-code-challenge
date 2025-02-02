class Band:
    all = []
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = None
        self._hometown_set = False
        self.hometown = hometown
        Band.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise Exception("name must be a non-empty string")
        self._name = name

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if self._hometown_set:
            raise AttributeError("Hometown is immutable after being set.")
        if not isinstance(value, str) or len(value) < 1:
            raise Exception("hometown must be a non-empty string")
        self._hometown = value
        self._hometown_set = True
    


    


    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        list_of_venues = []
        for concert in self.concerts():
            if concert.venue not in list_of_venues:
                list_of_venues.append(concert.venue)
        return list_of_venues

    def play_in_venue(self, venue, date):
        return Concert(date=date, band=self, venue=venue)
        

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    all = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str) or len(date) < 1:
            raise Exception("date must be a non-empty string")
        self._date = date

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        if not isinstance(band, Band):
            raise Exception("band must be a Band instance")
        self._band = band

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        if not isinstance(venue, Venue):
            raise Exception("venue must be a Venue instance")
        self._venue = venue

    def hometown_show(self):
        if self.band.hometown == self.venue.city:
            return True
        else:
            return False

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all = []
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise Exception("name must be a non-empty string")
        self._name = name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not isinstance(city, str) or len(city) < 1:
            raise Exception("city must be a non-empty string")
        self._city = city
    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        list_of_bands = []
        for concert in self.concerts():
            if concert.band not in list_of_bands:
                list_of_bands.append(concert.band)
        return list_of_bands
    
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
