from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
# password = "anushka@2002"
password = quote_plus("anushka@2002")
host = "localhost"
port = "3306"
database = "sales_db"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)


try:
    connection = engine.connect()
    print("Connected to MySQL successfully!")
    connection.close()
except Exception as e:
    print("Connection failed!")
    print(e)