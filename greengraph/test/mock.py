from mock import patch
import requests

#import sys
#sys.path.insert(0, '/home/ioana/Greengraph/greengraph')
#import map
from ..map import Map
from ..graph import Greengraph

ioana = Map(51.5073509, -0.1277583)

with patch.object(requests,'get') as mock_get:
    london_map=Map(51.5073509, -0.1277583)
    print mock_get.mock_calls

