import json
import random

import pymysql

# read the config.json file
import generator

with open("config.json", "r") as f:
    config = json.loads(f.read())


# Generate random data for mysql database
def generate_data():
    # Connect to the database
    connection = pymysql.connect(host=config.get("MMYSQL_DATABASE_HOST"),
                                 user=config.get("MYSQL_DATABASE_USER"),
                                 password=config.get("MYSQL_DATABASE_PASSWORD"),
                                 db=config.get("MYSQL_DATABASE_NAME"),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            for i in range(config.get("NUMBER_OF_ROWS")):
                sql = build_insert_statement()
                cursor.execute(sql)
                connection.commit()
    finally:
        connection.close()


def build_insert_statement():
    columns = config.get("COLUMNS")
    columns_str = ""
    values_str = ""
    for column in columns:
        columns_str += column.get("NAME") + ", "
        if column.get("TYPE") == "ENUM":
            values_str += random.choice(column.get("ALLOWED_VALUES")) + ", "
        else:
            value = generator.generate(column.get("TYPE"))
            if column.get("UNIQUE"):
                value = str(value) + str(random.randint(0, 9999999999))
            values_str += "'" + value + "', " if isinstance(value, str) else str(value) + ", "
    columns_str = "(" + columns_str[:-2] + ")"
    values_str = "VALUES(" + values_str[:-2] + ")"
    return "INSERT INTO " + config.get("MYSQL_DATABASE_TABLE_NAME") + columns_str + " " + values_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_data()
