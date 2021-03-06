import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(here, '../../vendored'))

from interscraped import consistency_scraper

# Scraper args
bucket_name = os.environ['BUCKET_NAME']
obj_path = os.environ['CONSISTENCY_OBJECT_PATH']
url = os.environ['CONSISTENCY_URL']


def scraper(event, context):
    return consistency_scraper(
        url,
        bucket_name,
        obj_path
    )
