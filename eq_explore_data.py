import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data
filename = 'data/raw_eq_data.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

# Loading the data and displaying it in a format that's easier to read
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


mag_size = []
for mag in mags:
    try:
        result = mag * 5
    except TypeError:
        print('nope')
    else:
        if mag > 0:
            mag_size.append(result)


# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': mag_size,    
        'color': mag_size,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')