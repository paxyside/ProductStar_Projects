import requests
from pprint import pprint
import random



API_KEY = "9QXvI-qJroBCkqYw4T-LGjltNi-BpCMBrCvVCfM8sPU"
image_to_find = "cat"
url = f"https://api.unsplash.com/search/photos/?client_id={API_KEY}&query={image_to_find}"
response = requests.get(url)
data = response.json()
#pprint(data)

from PIL import Image
from io import BytesIO
random_hit = random.choice(data['results'])
image_url = random_hit["urls"]["regular"]
image_data = requests.get(image_url).content
img = Image.open(BytesIO(image_data))
img.show()