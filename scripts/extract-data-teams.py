# Add src to the system path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# import libraries
import cfb
import requests

def main():
    # prep url and headers
    url = "https://api.collegefootballdata.com/teams/fbs"
    headers = cfb.prep_headers()
    # call api for 2000 - 2023 teams
    json_list = []
    for i in range(2000, 2024, 1):
        # set year parameter
        params = {'year' : i}
        # hit api
        response = requests.get(url, params=params, headers = headers)
        # strip json from response if successful
        if response.status_code == 200:
            teams_json = response.json()
            json_list.append([i, teams_json])
        else:
            json_list.append([i, ''])
    # print sample to see if it works..
    x = json_list[0][1]
    print(x)
    
if __name__ == '__main__':
    main()