import os
from dotenv import load_dotenv

load_dotenv()
class Data:

    NAME = os.getenv("NAME")
    LASTNAME = os.getenv("LASTNAME")