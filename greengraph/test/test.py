import yaml
import os
from nose.tools import assert_equal
from nose.tools import assert_raises
from nose.tools import assert_almost_equal
from ..map import Map
from ..graph import Greengraph

def test_geolocate():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','samples_geolocate.yaml')) as fixtures_file:
	    fixtures = yaml.load(fixtures_file)
	    for fixture in fixtures:
		    location = fixture.pop('location')    
		    lats = fixture.pop('lats')
		    longs = fixture.pop('longs')
		    answer = (lats,longs)
	    
		    geo = Greengraph(0.0,0.0)
		    assert_equal(geo.geolocate(location), answer)
    

#test_geolocate()

def test_location_sequence():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','samples_location_sequence.yaml')) as fixtures_file:
	    fixtures = yaml.load(fixtures_file)
	    for fixture in fixtures:
		    start = fixture.pop('start') 
		    end = fixture.pop('end')
		    steps = fixture.pop('steps')  
		    lats1 = fixture.pop('lats1')
		    longs1 = fixture.pop('longs1')		    
		    
		    geo = Greengraph(0.0,0.0)
		    answer = geo.location_sequence(geo.geolocate(start),geo.geolocate(end),steps)
		    assert(answer[0][0]==lats1 and answer[0][1]==longs1)	

#test_geolocate()	


def test_green_between():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','samples_green_between.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            steps = fixture.pop('steps') 
            answer = fixture.pop('answer')  

            geo = Greengraph(0.0,3.0)
            answer = geo.green_between(steps)
            assert_equal(geo.green_between(steps), answer) 

#test_geolocate()

geo = Map(51.5073509, -0.1277583, satellite=True, zoom=10, size=(2,2))
print geo.green(1.1)


def test_green():
	with open(os.path.join(os.path.dirname(__file__),'fixtures','samples_green.yaml')) as fixtures_file:
		fixtures = yaml.load(fixtures_file)
		for fixture in fixtures:
			lat = fixture.pop('lat')
			longs = fixture.pop('longs')
			satellite = fixture.pop('satellite')
			zoom = fixture.pop('zoom')
			size = tuple(fixture.pop('size'))
			threshold = fixture.pop('threshold')
			answer = fixture.pop('answer')
			
			geo = Map(lat, longs, satellite, zoom, size)
			assert_equal(sum(sum(geo.green(threshold)==True)), size[0]*size[1])

#test_geolocate()


