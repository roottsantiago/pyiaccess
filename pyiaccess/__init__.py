import os
from dotenv import load_dotenv
from pyiaccess.settings import BASE_DIR

print('BASE_DIR', BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, ".back.env"))
