"""
executeable file for migrating database
"""
import logging
import os
import traceback

from dotenv import load_dotenv

if __name__ == "__main__":
    try:
        # load env from .env file at repository directory root
        load_dotenv()

        # migrate database
        os.system("alembic upgrade head")
        print("Migrate database success!")

        # migrate testing database
        os.environ["PROJECT_ENV"] = "test"
        os.system("alembic upgrade head")
        print("Migrate testing database success!")

    except Exception as err:
        logging.error(traceback.format_exc())
