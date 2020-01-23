import geocoder
def place():
    g = geocoder.ip('me')
    return g.city
def locate():
    g = geocoder.ip('me')
    return g.latlng
