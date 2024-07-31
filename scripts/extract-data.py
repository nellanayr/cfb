# Add src to the system path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from cfb import get_api_key

api_key = get_api_key()