import os
import sys
import boto3

# here = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, os.path.join(here, '../../vendored'))


from psycopg2 import connect

s3 = boto3.client('s3')


def get_csv_data(obj_key):
    data = s3.get_object(Bucket=os.environ['BUCKET_NAME'], Key=obj_key)
    return data.get('Body')


def main(event):
    # Get environment variables
    db_name = 'boof_2'

    # Setup connection string
    connect_string = 'dbname={}'.format(
        db_name,
    )

    # Connect to the database
    try:
        conn = connect(connect_string)
    except RuntimeError as err:
        print('Failed to connect to the db', err)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    content = get_csv_data(event['obj']['key'])
    print(content, 'content')
    try:
        cur.copy_from(
            content.read(),
            'consistency_rating',
            columns=('full_name','start_pct','c_rating','ppr_start_pct','fanptsgame','start_ct','stud_ct','stiff_ct','sat_ct','pos'),
            sep=","
        )

    except RuntimeError as err:
        print('Command Failed: ', err)
        conn.rollback()
        conn.close()

    # Commit the changes and close communication with the database
    print('Script completed successfully. Exiting...')
    conn.commit()
    cur.close()
    conn.close()


event = {
    'obj': {
        'key': 'current_season/consistency_ratings/2015_2017.csv'
    }
}
main(event)
