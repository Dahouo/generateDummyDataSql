import csv
import json
import os
import random

import pymysql
import generator

# read the config.json file
with open("config.json", "r") as f:
    config = json.loads(f.read())


# Generate random data for mysql database
def generate_data():
    columns = config.get("COLUMNS")
    columns_str = list()
    for column in columns:
        columns_str.append(column.get("NAME"))

    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(columns_str)
        for i in range(config.get("NUMBER_OF_ROWS")):
            writer.writerow(build_values(columns))
    connection = pymysql.connect(host=config.get("MYSQL_DATABASE_HOST"),
                                 user=config.get("MYSQL_DATABASE_USER"),
                                 password=config.get("MYSQL_DATABASE_PASSWORD"),
                                 db=config.get("MYSQL_DATABASE_NAME"),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 local_infile=True,
                                 ssl={"fake_flag_to_enable_tls": True})

    try:
        with connection.cursor() as cursor:
            sql = "LOAD DATA LOCAL INFILE 'data.csv' INTO TABLE " + config.get("MYSQL_DATABASE_TABLE_NAME") + \
                  " FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES"
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()
        os.remove("data.csv")


def build_values(columns):
    values_str = list()
    for column in columns:
        if column.get("TYPE") == "ENUM":
            values_str.append(random.choice(column.get("ALLOWED_VALUES")))
        else:
            value = generator.generate(column.get("TYPE"))
            if column.get("UNIQUE"):
                value = str(value) + str(random.randint(0, 9999999999))
            if column.get("MIN_LENGTH") and len(value) < column.get("MIN_LENGTH"):
                value = value + str(random.randint(0, 9)) * (column.get("MIN_LENGTH") - len(value))
            if column.get("MAX_LENGTH") and len(value) > column.get("MAX_LENGTH"):
                value = value[:column.get("MAX_LENGTH")]
            values_str.append(value)
    return values_str


if __name__ == '__main__':
    generate_data()
