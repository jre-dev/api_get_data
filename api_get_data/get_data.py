import os

import geojson
import requests

from csv_to_geojson import create_geojson


def get_data(file_name: str, url: str, csv=False, offset=None):
    """

    :param csv:
    :param offset:
    :param url:
    :param file_name:
    """
    attribute_error_message = "Attribute Error"

    try:
        response = requests.get(url, allow_redirects=True)
        if csv:
            csv_file_name = 'data.csv'
            open(csv_file_name, 'wb').write(response.content)
            create_geojson(csv_file_name, file_name)
            if os.path.isfile(csv_file_name):
                os.remove(csv_file_name)
            else:
                print("Error: %s file not found" % csv_file_name)
            return
        data = response.json()

        if offset:
            data = response.json()
            i = 0
            while response.json()["features"]:
                url = url.replace(f"resultOffset={i}", f"resultOffset={i + offset}")
                response = requests.get(url)
                data["features"].extend(response.json()["features"])
                i += offset
            print(len(data["features"]))
            with open(file_name, 'w', encoding='utf-8') as f:
                geojson.dump(data, f, ensure_ascii=False)

        else:
            print(len(data["features"]))
            with open(file_name, 'w', encoding='utf-8') as f:
                geojson.dump(data, f, ensure_ascii=False)
    except AttributeError:
        print(attribute_error_message)


if __name__ == "__main__":
    get_data(
        f'../../tests/tests.geojson',
        "https://services6.arcgis.com/6jU7RmJig2Wwo1b0/ArcGIS/rest/services/Ladesaeulenregister/FeatureServer/7/query?where=&objectIds=&time=&geometry=%7B%0D%0A++%22xmin%22%3A+619491.991483609%2C%0D%0A++%22ymin%22%3A+5965153.22910007%2C%0D%0A++%22xmax%22%3A+1733428.14197738%2C%0D%0A++%22ymax%22%3A+7373502.38547309%2C%0D%0A++%22spatialReference%22%3A+%7B%0D%0A++++%22wkid%22%3A+102100%0D%0A++%7D%0D%0A%7D&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=0&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=",
        False, 2000
    )
