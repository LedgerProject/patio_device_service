import hashlib
from requests.auth import HTTPBasicAuth

TESTING_BACK = True
MOCK_SENSORS = True

# If not IOTA, Zenroom will be used
IOTA = False

power_unit = 'W'

if TESTING_BACK:
    base_backend_url = "http://localhost:8000"
else:
    base_backend_url = "https://back.supervecina.com"

# Community 1 token
community_token = "c78760cf-7716-4045-8d30-186821d9c8f5"
community_unique_id = hashlib.md5(community_token.encode()).hexdigest()

IOTA_WATT_URL = "http://793108fb4d46.sn.mynetname.net:17777/"

IOTA_WATT_AUTH = HTTPBasicAuth('admin', 'wqFZdgwub9y%')

WAITING_TIME = 5

# This dict is fixed. But in the future it'll be get from SaaS API to get data
# for the specific community
# In the case of 'neighbour_X', X is the UserCommunity ID from backend
SENSORS = None
if not IOTA_WATT_URL:
    SENSORS = {"generation": {"generation_1": ""},
            "consumption": {"common_place_1": "0x40",  # value should be the addr of the sensor
                            # 4 is the id of demo usercommunity for Community 1
                            "neighbour_4": "0x41"
                            },
            }
else:
    SENSORS = {"generation": {"generation_1": "Generator"},
           "consumption": {"common_place_1": "Letrero",  # value should be the id of the sensor
                           # 4 is the id of demo usercommunity for Community 1
                           "neighbour_4": "Fotocelula"
                           },
           }
