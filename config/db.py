import databases

try:
    DATABASE_URL = 'sqlite:///db.s3db'
    database = databases.Database(DATABASE_URL)


except Exception as e:
    print(e)
