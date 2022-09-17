import json
import pickle
import numpy as np

__locations = None
__area_type = None
__data_columns = None
__model = None


def get_estimates_price(location, area_type, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
        at_index = __data_columns.index(area_type.lower())
    except:
        loc_index = -1
        at_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if at_index >= 0:
        x[at_index] = 1
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)


def get_atype_name():
    return __area_type


def get_columns_names():
    return __data_columns


def get_location_name():
    return __locations


def load_stuff():
    print("loading stuffs.......")
    global __locations
    global __area_type
    global __data_columns
    with open("../data/columns.json", "r") as f:
        __data_columns = json.load(f)
        __area_type = __data_columns[3:6]
        __locations = __data_columns[6:]
    global __model

    if __model is None:
        with open('../data/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
