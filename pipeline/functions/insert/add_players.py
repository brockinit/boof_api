import os
import sys
import boto3

# here = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, os.path.join(here, '../../vendored'))


from psycopg2 import connect

s3 = boto3.client('s3')


def get_csv_data(obj_key):
    data = s3.get_object(Bucket=os.environ['BUCKET_NAME'], Key=obj_key)
    return data.get('Body').read().decode('utf-8').splitlines()


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

    for line in content:
        line_values = line.split(',')
        try:
            player_name = line_values[2].strip()
            player_pos = line_values[3].strip()
            player_id = line_values[1].strip()

            insert_command = 'INSERT INTO player (id, full_name, pos) VALUES (%s,%s, %s) ON CONFLICT (id) DO NOTHING'
            arg_tuple = (player_id, player_name, player_pos)
            cur.execute(insert_command, arg_tuple)

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
        'key': 'current_season/player_data_game/2017/1/TE.csv'
    }
}
main(event)
