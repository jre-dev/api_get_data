import requests
import pandas
import numpy
from geojson import Point, Feature, FeatureCollection, dumps


def create_geojson(csv_file_name, output_file_name):
    df = pandas.read_csv(csv_file_name, dtype=str).fillna('')
    lat = df['latitude']
    lng = df['longitude']
    df = df.drop(columns=['latitude', 'longitude'])

    feat_list = []
    failed = []
    for i in range(0, len(df.index)):
        props = remove_np_from_dict(dict(df.loc[i]))
        try:
            f = Feature(geometry=Point((float(lng[i]), float(lat[i]))),
                        properties=props)
            feat_list.append(f)
        except ValueError:
            failed.append(props)

    collection = FeatureCollection(feat_list)
    with open(output_file_name, 'w') as f:
        f.write(dumps(collection))

    return output_file_name


def remove_np_from_dict(d):
    """numpy int64 objects are not serializable so need to convert values first."""
    new = {}
    for key, value in d.items():
        if isinstance(key, numpy.int64):
            key = int(key)
        if isinstance(value, numpy.int64):
            value = int(value)
        new[key] = value
    return new


def convert_numpy(val):
    if isinstance(val, numpy.int64):
        return int(val)


CSV_URL = "https://chargepoints.dft.gov.uk/api/retrieve/registry/format/csv/"
r = requests.get(CSV_URL, allow_redirects=True)
open('data.csv', 'wb').write(r.content)

if __name__ == "_-main__":
    create_geojson("data.csv", "test.geojson")
