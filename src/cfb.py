from dotenv import load_dotenv
import os

def get_api_key():
    load_dotenv()                           # load environment variables
    api_key = os.getenv('CFB_API_KEY')      # get api key
    return api_key                          # return api key