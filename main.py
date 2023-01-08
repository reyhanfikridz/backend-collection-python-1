"""
main executeable file
"""
import os

from dotenv import load_dotenv

if __name__ == "__main__":
    try:
        # load env from .env file at repository directory root
        load_dotenv()

        # run server with uvicorn
        os.system((
            f"uvicorn app.app:app --host={os.getenv('APP_HOST')} "
            f"--port={os.getenv('APP_PORT')} --reload"
        ))

    except KeyboardInterrupt:
        # if there's keyboard interrupt (CTRL + C), do not output the log
        pass
