import requests
from bs4 import BeautifulSoup
import re

import numpy as np
import pandas as pd

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
}


def fetch_reviews(**kwargs):
    # If arguments has passed - create business id
    if kwargs:
        location = kwargs["location"].lower().strip()
        name = "-".join(kwargs["name"].lower().strip().split())
        business_id = "-".join((name, location))
    else:
        business_id = "meat-a-greet-praha"

    url = "https://www.yelp.com/biz/" + business_id

    r = requests.get(url)

    if not r:
        raise ValueError("Bad request")

    soup = BeautifulSoup(r.text, "html.parser")
    comment_regex = re.compile(".*comment.*")
    comments = soup.find_all("p", {"class": comment_regex})
    reviews = [comment.text for comment in comments]

    df = pd.DataFrame(np.array(reviews), columns=["reviews"])

    return df


if __name__ == "__main__":
    fetch_reviews()
