import json
import os
from urllib.request import urlopen, urlretrieve

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")


def search_photos(q, n=10, sort="interestingness-desc"):
    params = {
        "method": "flickr.photos.search",
        "api_key": API_KEY,
        "text": q,
        "per_page": n,
        "sort": sort,
        "format": "json",
        "nojsoncallback": "1",
    }
    response = requests.get("https://api.flickr.com/services/rest/", params=params)
    response_json = response.json()

    save(response_json, q)
    return response_json


def save(response_json, q):
    path = "data/{}.json".format(q)

    with open(path, "w") as f:
        json.dump(response_json, f)

    print("save to {}".format(path))


def get_id_and_url(photo):
    url = "https://farm{}.staticflickr.com/{}/{}_{}.jpg".format(
        str(photo["farm"]), photo["server"], photo["id"], photo["secret"]
    )
    return photo["id"], url
