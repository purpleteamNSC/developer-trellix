from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_access_token(client_id, client_secret, scope, audience):
    url = 'https://iam.mcafee-cloud.com/iam/v1.1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'scope': scope,
        'audience': audience
    }
    auth = (client_id, client_secret)
    
    response = requests.post(url, headers=headers, data=data, auth=auth)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Error: {response.status_code}")
        return None


client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
scope = os.getenv('SCOPES')
audience = 'trellix'

access_token = get_access_token(client_id, client_secret, scope, audience)
if access_token:
    print("Access token:", access_token)
else:
    print("Failed to get access token.")
