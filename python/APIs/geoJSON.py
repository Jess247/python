import urllib.request
import urllib.parse
import urllib.error
import json

# not working without a key
serviceUrl = 'https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY'

while True:
    address = input('Please enter a location: ')
    if len(address) < 1:
        break

    url = serviceUrl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != "OK":
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
