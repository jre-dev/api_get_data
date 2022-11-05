__version__ = 'dev'

import json
import os
import pkg_resources
from src.get_data import get_data


def update_data(directory="data"):
    path = os.path.join(os.getcwd(), directory)
    if not os.path.isdir(path):
        os.mkdir(path)
    url_data_path = pkg_resources.resource_filename(__name__, 'data/urls.json')
    with open(url_data_path, 'r', encoding='utf-8') as f:
        url_data = json.load(f)
        for url in url_data:
            get_data(f"{os.path.join(path, directory)}{url_data[url][0]}", url_data[url][1], url_data[url][2],
                     url_data[url][3])


if __name__ == '__main__':
    update_data("test_data")
