class Band:
    all = []
    def __init__(self, name, hometown):
        self.name = name
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
    def hometown(self, hometown):
        if not isinstance(hometown, str) or len(hometown) < 1:
            raise Exception("hometown must be a non-empty string")
        self._hometown = hometown
    


    


    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        pass

    def play_in_venue(self, venue, date):
        pass
        

    def all_introductions(self):
        pass


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
    def __init__(self, name, city):
        self.name = name
        self.city = city
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
        return [concert.band for concert in self.concerts()]
