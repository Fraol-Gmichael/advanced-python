"""I can use grep -nr "location=" to find location inside some function
Or I can use grep -nr "location =" to find a variable called location
"""
location = "Ethiopia"


def set_location(location):
    pass


set_location(location="ethiopia")
