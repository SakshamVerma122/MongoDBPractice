import os
from dotenv import load_dotenv,find_dotenv

# if we store information using enviroment variable then we
# will be able to share the code keeping the password secretly
# stored in our local machine

load_dotenv(find_dotenv())


# os.environ is a dictionary containing 
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user)
print(db_password)