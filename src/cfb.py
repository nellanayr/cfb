from dotenv import load_dotenv
import os

def get_api_key():
    load_dotenv()                           # load environment variables
    api_key = os.getenv('CFB_API_KEY')      # get api key
    return api_key                          # return api key

def prep_headers():
    api_key = get_api_key()                 # get api key
    headers = {                             # prep headers
        "Authorization": f"Bearer {api_key}"
    }
    return headers

