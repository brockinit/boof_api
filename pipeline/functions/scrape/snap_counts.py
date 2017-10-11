import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(here, '../../vendored'))

from interscraped import snap_counts_scraper

# Scraper args
credentials = {
    'email': os.environ['FANT_DATA_EMAIL'],
    'password': os.environ['FANT_DATA_PASSWORD']
}
bucket_name = os.environ['BUCKET_NAME']
obj_path = os.environ['SNAP_COUNT_OBJECT_PATH']
years = [{'2017': 0}]
weeks = [int(os.environ['CURRENT_WEEK'])]


def scraper(event, context):
    return snap_counts_scraper(
        credentials,
        bucket_name,
        obj_path,
        years=years,
        weeks=weeks
    )
