__version__ = '0.1.0'

from src.get_data import get_data
import json
# websites = {
#     'germany': {
#         'dataset_germany': 'https://services6.arcgis.com/6jU7RmJig2Wwo1b0/ArcGIS/rest/services/Ladesaeulenregister/FeatureServer/7/query?where=&objectIds=&time=&geometry=%7B%0D%0A++%22xmin%22%3A+619491.991483609%2C%0D%0A++%22ymin%22%3A+5965153.22910007%2C%0D%0A++%22xmax%22%3A+1733428.14197738%2C%0D%0A++%22ymax%22%3A+7373502.38547309%2C%0D%0A++%22spatialReference%22%3A+%7B%0D%0A++++%22wkid%22%3A+102100%0D%0A++%7D%0D%0A%7D&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=0&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token='},
#     'france': {'datasets_france': 'https://transport.data.gouv.fr/api/datasets',
#                'dataset_france_147': 'https://www.data.gouv.fr/fr/datasets/r/7eee8f09-5d1b-4f48-a304-5e99e8da1e26'},
#     'uk': {'dataset_uk': 'https://chargepoints.dft.gov.uk/api/retrieve/registry/format/json/'}
# }
if __name__ == '__main__':
    with open("../data/urls.json", 'r', encoding='utf-8') as f:
        urls = json.load(f)
        print(type(urls))
        print(urls)
        directory = "../data/"

        for url in urls:
            get_data(f"{directory}{urls[url][0]}", urls[url][1], urls[url][2], urls[url][3])

