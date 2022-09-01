from dotenv import load_dotenv
import logging
import os

load_dotenv()
# Databse configs
DB_NAME = os.getenv("DB_NAME", 'gomerce')
DB_TEST_NAME = os.getenv("DB_TEST_NAME", 'gomerce-test')
DB_USER = os.getenv("DB_USER", 'postgres')
DB_PASSWORD = os.getenv("DB_PASSWORD", '')
DB_HOST = os.getenv("DB_HOST", 'localhost')
DB_PORT = os.getenv("DB_PORT", 5432)

POSTGRES = {
    "user": DB_USER,
    "pw": DB_PASSWORD,
    "host": DB_HOST,
    "port": DB_PORT,
    "db": DB_NAME,
}

DB_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES


DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/application")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "db")

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)