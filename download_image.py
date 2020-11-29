import glob
import json
import os
import re
import time
import urllib.request

import flickr


def download(url, path):
    try:
        with urllib.request.urlopen(url) as w:
            data = w.read()
            with open(path, mode="wb") as f:
                f.write(data)
    except Exception as e:
        print("failed to download {}: {}".format(url, e))


if __name__ == "__main__":
    file_paths = glob.glob("data/*.json")

    if not os.path.exists("data/images"):
        os.makedirs("data/images")

    for path in file_paths:
        file_name = re.search(r"data/(.+).json", path).group(1)

        dir = "data/images/{}".format(file_name)
        if not os.path.exists(dir):
            os.makedirs(dir)

        with open(path, "r") as f:
            resource = json.load(f)
            for i, v in enumerate(resource["photos"]["photo"]):
                id, url = flickr.get_id_and_url(v)
                path = "{}/{}.jpg".format(dir, id)
                download(url, path)
                time.sleep(1)

        print("complete {}".format(file_name))
