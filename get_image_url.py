import urllib.request
import time

import flickr

N = 5
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
        flickr.search_photos(q, n=N)
        time.sleep(1)