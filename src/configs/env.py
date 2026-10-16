import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABSE_URL")