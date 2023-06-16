class Point:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


def location(latitude: float, longitude: float) -> Point:
    return Point(latitude, longitude)


location(12, 42)
