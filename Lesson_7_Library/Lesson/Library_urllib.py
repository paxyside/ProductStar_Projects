import urllib.request
import json
import random
from pprint import pprint
API_KEY = "9QXvI-qJroBCkqYw4T-LGjltNi-BpCMBrCvVCfM8sPU"
image_to_find = "russia"
url = f"https://api.unsplash.com/search/photos/?client_id={API_KEY}&query={image_to_find}"
def get_data(url):
    req = urllib.request.Request(url, headers={"Accept-Version": "v1"})
    response = urllib.request.urlopen(req)
    data_string = response.read().decode()
    try:
        data = json.loads(data_string)
        return data
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding response: {e}")
        return None
    
data = get_data(url)
if data is not None:
    # Действия, которые следует выполнить в случае успешного получения данных
    #pprint(data)
    random_hit = random.choice(data['results'])
    pprint(random_hit)
    
else:
    # Действия, которые следует выполнить в случае ошибки
    print("Error getting data from API")
    
image_url = random_hit["urls"]["regular"]
print(image_url)

req = urllib.request.Request(image_url, headers={"Accept-Version": "v1"})
image_data = urllib.request.urlopen(req).read()
from IPython.display import Image
Image(image_data, width=500)
