# -*- coding: utf-8 -*-
import re, math

R = 6371.0

# NOTE: FUCK UNICODE IN PYTHON. FUCK IT ALL
# https://github.com/Empire-of-Code-Puzzles/checkio-empire-earth-distances
# haversine formula
def distance(first, second):
    lat1, lon1 = [a for a in re.split(u",| ", first) if a]
    lat2, lon2 = [a for a in re.split(u",| ", second) if a]

    print lat1
    d = re.split(u"\xb0|\u2032|\u2033", lat1)
    lat_dir1 = d[-1].strip(",")
    lat_d1 = float(d[0]) + float(d[1])/60.0 + float(d[2])/3600.0

    d = re.split(u"\xb0|\u2032|\u2033", lat2)
    lat_dir2 = d[-1].strip(",")
    lat_d2 = float(d[0]) + float(d[1])/60.0 + float(d[2])/3600.0

    dlat = 0
    if lat_dir1 == lat_dir2:
        dlat = abs(lat_d1 - lat_d2) * math.pi / 180.0
    else:
        dlat = abs(lat_d1 + lat_d2) * math.pi / 180.0
    print dlat

    d = re.split(u"\xb0|\u2032|\u2033", lon1)
    lon_dir1 = d[-1].strip(",")
    lon_d1 = float(d[0]) + float(d[1])/60.0 + float(d[2])/3600.0

    d = re.split(u"\xb0|\u2032|\u2033", lon2)
    lon_dir2 = d[-1].strip(",")
    lon_d2 = float(d[0]) + float(d[1])/60.0 + float(d[2])/3600.0

    dlon = 0
    if lon_dir1 == lon_dir2:
        dlon = abs(lon_d1 - lon_d2) * math.pi / 180.0
    else:
        dlon = abs(lon_d1 + lon_d2) * math.pi / 180.0
    print dlon

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat_d1*math.pi/180.0) * math.cos(lat_d2*math.pi/180.0) * math.sin(dlon/2) * math.sin(dlon/2);
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));

    return R * c


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
    assert almost_equal(
        distance(u"48°27′0″N,34°59′0″E", "15°47′56″S 47°52′0″W"), 10801.622299208242), "foo"

    print("All done? Earn rewards by using the 'Check' button!")
