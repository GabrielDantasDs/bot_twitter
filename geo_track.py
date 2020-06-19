from geopy.geocoders import Nominatim


class geo_tracker :
    def __init__(self):
        self.geolocator = Nominatim   (user_agent = "Tweepy-experience")
        geolocator = self.geolocator
        self.location = geolocator.geocode("Brasil")
        location = self.location

