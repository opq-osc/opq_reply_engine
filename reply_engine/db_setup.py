import sqlite3
import os, json
import re

cur_file_dir = os.path.dirname(os.path.realpath(__file__))
db_schema = ''

try:
    with open(os.path.join(cur_file_dir, 'config.json'), 'r', encoding='utf-8') as f:
        config = json.load(f)
        db_schema = config['db_schema']
except:
    print('Cannot resolve db_schema name from config.json')
    raise


def update_db():

    conn = sqlite3.connect(os.path.join(cur_file_dir, db_schema))
    cur = conn.cursor()

    try:
        with open(os.path.join(cur_file_dir, 'db_setup'), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if re.match("^#.*", line):
                    continue
                print('Executing: ', line)
                cur.execute(line)
    except:
        print('Failed to execute DB setup')
        raise
    conn.commit()
    conn.close()


if __name__ == '__main__':
    update_db()
