import os
import time

from dotenv import load_dotenv

import flickr

load_dotenv()

os.environ.get("N")

PATH = "data/queries.txt"


def get_queries(path):
    queries = []
    with open(path) as f:
        for line in f:
            q = line.strip()
            queries.append(q)
    return queries


if __name__ == "__main__":
    queries = get_queries(PATH)
    for q in queries:
        flickr.search_photos(q, n=N, sort="relevance")
        time.sleep(1)
