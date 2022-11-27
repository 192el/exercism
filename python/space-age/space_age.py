year = 31557600
planets = {
    "earth": 1, "mercury": 0.2408467, "venus": 0.61519726, "mars": 1.8808158,
    "jupiter": 11.862615, "saturn": 29.447498, "uranus": 84.016846, "neptune":  164.79132
}
class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    def on_earth(self):
        return round((self.seconds / planets["earth"]) / year, 2)
    def on_mercury(self):
        return round((self.seconds / planets["mercury"]) / year, 2)
    def on_venus(self):
        return round((self.seconds / planets["venus"]) / year, 2)
    def on_mars(self):
        return round((self.seconds / planets["mars"]) / year, 2)
    def on_jupiter(self):
        return round((self.seconds / planets["jupiter"]) / year, 2)
    def on_saturn(self):
        return round((self.seconds / planets["saturn"]) / year, 2)
    def on_uranus(self):
        return round((self.seconds / planets["uranus"]) / year, 2)
    def on_neptune(self):
        return round((self.seconds / planets["neptune"]) / year, 2)
