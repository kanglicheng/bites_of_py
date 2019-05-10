cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    temp = []
    for model in cars['Jeep']:
        temp.append(model)
    return ", ".join(m for m in temp)


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_models = []
    for v in cars.values():
        first_models.append(v[0])
    return first_models


import re
def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matches = []
    pattern = re.compile(grep, re.IGNORECASE)
    for v in cars.values():
        for car in v:
            if re.search(pattern, car):
                matches.append(car)
    return sorted(matches)

def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for c, v in cars.items():
        cars[c] = sorted(v)
    return cars
