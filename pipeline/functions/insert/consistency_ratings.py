import os
import sys
import boto3

# here = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, os.path.join(here, '../../vendored'))


from psycopg2 import connect

s3 = boto3.client('s3')


def get_lines(obj_key):
    data = s3.get_object(Bucket=os.environ['BUCKET_NAME'], Key=obj_key)
    print(data, 'DATA')


def main(event):
    # Get environment variables
    db_name = 'boof'

    # Setup connection string
    connect_string = 'dbname={}'.format(
        db_name,
    )

    # Connect to the database
    # try:
    #     conn = connect(connect_string)
    # except RuntimeError as err:
    #     print('Failed to connect to the db', err)

    # Open a cursor to perform database operations
    # cur = conn.cursor()

    error_players = []
    print(event, "EVENT")
    content = get_lines(event['obj']['key'])

    # for line in content:
    #     line_values = line.split(',')

        # Search for player in the database
        # select_command = "SELECT * FROM player WHERE UPPER(full_name) = %s or UPPER(REPLACE(full_name, '.', '')) = %s or UPPER(REPLACE(full_name, '-', '')) = %s"
        # try:
        #     player_name = line_values[0].strip()
        #     player_pos = line_values[len(line_values) - 1].strip()

        #     cur.execute(select_command, (player_name.upper(),player_name.upper(),player_name.upper(),))
        #     result = cur.fetchone()

        #     # Warning: Player not found in player table
        #     if result is None:
        #         if player_name[1] != ' ':
        #             error_players.append(player_name)
        #             # raise RuntimeError


        #     else:
        #         # Add player_id to the row
        #         row_values = line + ',' + str(result[0])
        #         print(row_values, 'values')
        #         insert_command = "INSERT INTO consistency_rating (full_name,start_pct,c_rating,ppr_start_pct,fanptsgame,start_ct,stud_ct,stiff_ct,sat_ct,pos,player_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        #         arg_tuple = ()
        #         for col in row_values.split(','):
        #             arg_tuple = arg_tuple + (col,)
        #         print(arg_tuple)
        #         cur.execute(insert_command, arg_tuple)

        # except RuntimeError as err:
        #     print('Command Failed: ', err)
        #     conn.rollback()
        #     conn.close()

    # Commit the changes and close communication with the database
    # print('Script completed successfully. Exiting...')
    # print(error_players, 'Errors')
    # conn.commit()
    # cur.close()
    # conn.close()


event = {
    'obj': {
        'key': 'current_season/consistency_ratings/2014_2017.csv'
    }
}
main(event)
