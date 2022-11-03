# generateDummyDataSql

Tool to generate dummy data for SQL databases.

## Usage
Edit the `config.json` file to your needs.

+ "MYSQL_DATABASE_HOST": The host of the database
+ "MYSQL_DATABASE_PORT": The port of the database
+ "MYSQL_DATABASE_USER": The user of the database
+ "MYSQL_DATABASE_PASSWORD": The password of the database
+ "MYSQL_DATABASE_NAME": The name of the database
+ "MYSQL_DATABASE_TABLE_NAME": The name of the table to insert the data into
+ "NUMBER_OF_ROWS": The number of rows to insert
+ "COLUMNS": The description of the columns to insert

### Column description
The column description is an array of objects. Each object describes one column. The tool allows you to specify the type of the column you want to insert and other properties.
The tool will generate random data for the column with the help of the [Faker](https://github.com/joke2k/faker) library.
The supported types are available in file `DataType.py`

Following properties are available for each column description:
* "NAME": The name of the column
* "TYPE": The type of the column
* "MIN_LENGTH": The minimum value for the column
* "MAX_LENGTH": The maximum value for the column
* "UNIQUE": If the column should be unique
* "ALLOWED_VALUES": The allowed values for the column if the column is of type `ENUM`

Following types are supported:
* NAME
* PHONE
* EMAIL
* ADDRESS
* POSTAL_CODE
* REGION
* COUNTRY
* WORD
* TEXT
* NUMBER
* AMOUNT
* CURRENCY_CODE
* ALPHA_NUMERIC
* UUID
* UUID_WITHOUT_HYPHEN
* DATE
* DATE_TIME
* BOOLEAN
* ENUM
* BIT
* UNIQUE_ID

### Config Example
```json
{
  "MYSQL_DATABASE_HOST": "localhost",
  "MYSQL_DATABASE_PORT": 3306,
  "MYSQL_DATABASE_USER": "root",
  "MYSQL_DATABASE_PASSWORD": "root",
  "MYSQL_DATABASE_NAME": "test",
  "MYSQL_DATABASE_TABLE_NAME": "test",
  "NUMBER_OF_ROWS": 100,
  "COLUMNS": [
    {
      "NAME": "id",
      "TYPE": "UNIQUE_ID",
      "MIN_LENGTH": 1,
      "MAX_LENGTH": 100,
      "UNIQUE": true
    },
    {
      "NAME": "name",
      "TYPE": "NAME",
      "MIN_LENGTH": 1,
      "MAX_LENGTH": 100
    },
    {
      "NAME": "role",
      "TYPE": "ENUM",
      "ALLOWED_VALUES": ["ADMIN", "USER"]
    }
```

## License
MIT

## Author
[Arnaud Ahouo](mailto:dahouo50@gmail.com)

## Acknowledgments
* [Faker](https://faker.readthedocs.io/en/master/) - The library used to generate random data

## Contributing
Feel free to contribute to this project by opening a pull request.
