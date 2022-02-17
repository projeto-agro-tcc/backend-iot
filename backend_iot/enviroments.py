from backend_iot.settings import BASE_DIR

#URI_MONGO = "mongodb://admin:123456@127.0.0.1:27017"
URI_MONGO = 'mongodb://root:ort4344svfa0098ii9o@localhost:27017'
DB_NAME = 'iot_monitoramento'
RECEIVED_DATADB = 'received_data'

COLLECTIONS_EMW = {
    "solar" : "emw_solar_radiation_irradiance",
    "pressure" : "emw_atm_pressure_pressure",
    "rain" : "emw_rain_level_length",
    "wind" : "emw_average_wind_speed_velocity",
    "gust" : "emw_gust_wind_speed_velocity",
    "dir" : "emw_wind_direction_angle",
    "temp" : "emw_temperature_temperature",
    "humid" : "emw_humidity_humidity",
    "lum" : "emw_luminosity_lux",
    "uv" : "emw_uv_dimensionless"
}

#database aws
database = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'backend_iot',
    'USER': 'root',
    'PASSWORD': '2021monitoramento',
    'HOST': 'localhost',
    'PORT': '3306',
}

#database localhost
# database = {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
# }
