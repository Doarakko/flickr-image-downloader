import glob
import json
import time
import re
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
    file_paths = glob.glob("data/*/*.json")

    for path in file_paths:
        dir_name = re.search(r"data/(.+)/.+", path).group(1)
        with open(path, "r") as f:
            resource = json.load(f)
            for i, v in enumerate(resource["photos"]["photo"]):
                url = flickr.get_url(v)
                path = "data/{}/{}_{}.jpg".format(dir_name, dir_name, i)
                download(url, path)
                time.sleep(1)

        print("complete {}".format(dir_name))
