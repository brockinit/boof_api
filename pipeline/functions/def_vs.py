import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(here, '../vendored'))

from interscraped import def_vs_scraper


def scraper(event, context):
    credentials = {
        'email': os.environ['FANT_DATA_EMAIL'],
        'password': os.environ['FANT_DATA_PASSWORD']
    }
    bucket_name = os.environ['BUCKET_NAME']
    obj_path = os.environ['DEF_VS_OBJECT_PATH']
    years = [{'2017': 0}]
    weeks = [int(os.environ['CURRENT_WEEK'])]

    return def_vs_scraper(
        credentials,
        bucket_name,
        obj_path,
        years=years,
        weeks=weeks
    )