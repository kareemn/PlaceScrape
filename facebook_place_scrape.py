import urllib
import simplejson

access_token = "YOUR_ACCESS_TOKEN"

place_search_url = 'https://graph.facebook.com/search?q=coffee&type=place&center=35.28,-120.659&distance=1000&access_token=%s' % access_token

f = urllib.urlopen(place_search_url)
contents = f.read()

myplaces = simplejson.loads(contents)
all_places = []

for place in myplaces['data']:
	name = place['name']
	place_id =  place['id']
	checkin_url = 'https://graph.facebook.com/%s?access_token=%s' % (place['id'], access_token)
	f2  = urllib.urlopen(checkin_url)
	checkin_contents = f2.read()
	thisplace = simplejson.loads(checkin_contents)
	num_checkins = thisplace['checkins']
	all_places.append( (name, place_id, num_checkins))
	

print sorted(all_places, key=lambda (x, y , z): -z)