import requests

url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={'is_holiday':0,'air_pollution_index':121,'humidity':89,'wind_speed':2,'wind_direction':329,'visibility_in_miles':1,'dew_point':1,'temperature':3888.8,'rain_p_h':1000,'snow_p_h':0,'clouds_all':40000,'weather_type':0.1,'weather_description':2.5,'Year':2014,'Month':10,'Day':12,'hour':9})
print(r.json()) # Writing on the Client Side,Everything should be Numerical