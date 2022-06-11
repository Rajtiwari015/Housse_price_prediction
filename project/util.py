import json
import pickle
import numpy as np

__locations=None
__data_columns=None
__model=None
def get_estimated_price(location,area,bed,resale,indoor,intercom,sports,power,gas,lift,vastu):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))

    x[0] = area
    x[1] = bed
    x[2] = resale
    x[3] = indoor
    x[4] = intercom
    x[5] = sports
    x[6] = power
    x[7] = gas
    x[8] = lift
    x[9] = vastu

    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations
def load_saved_artifacts():
    print("loading saved artifacts")
    global __locations
    global __data_columns
    with open("./artifacts/column.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[10:]

    global __model
    with open("./artifacts/final.pickle",'rb') as f:
        __model=pickle.load(f)

if __name__=='__main__':
    load_saved_artifacts()
    #print(get_location_names())
    print(get_estimated_price('location_horamavu',1500,1,1,0,0,0,1,1,1,0))