import random


def generate(data_type):
    from faker import Faker
    fake = Faker()

    datatype_dict = {
        "NAME": fake.name(),
        "PHONE": fake.phone_number(),
        "EMAIL": fake.email(),
        "ADDRESS": fake.address(),
        "POSTAL_CODE": fake.postcode(),
        "REGION": fake.state(),
        "COUNTRY": fake.country(),
        "WORD": fake.word(),
        "TEXT": fake.text(),
        "NUMBER": fake.random_number(),
        "AMOUNT": round(random.random(), 2),
        "CURRENCY_CODE": fake.currency_code(),
        "ALPHA_NUMERIC": fake.bothify(text='??##?#?##?'),
        "UUID": fake.uuid4(),
        "UUID_WITHOUT_HYPHEN": str(fake.uuid4()).replace("-", ""),
        "DATE": fake.date(),
        "DATE_TIME": fake.date_time(),
        "BOOLEAN": fake.boolean(),
        "BIT": random.randint(0, 1),
        "UNIQUE_ID": fake.unique.bothify(text='##########'),
    }

    return datatype_dict[data_type]
