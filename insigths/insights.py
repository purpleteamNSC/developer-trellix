from dotenv import load_dotenv
import requests
import os
from pprint import pprint


load_dotenv()

# variaveis de ambiente no .env
API_Key = os.getenv('TRELLIX_API_KEY')
Client_ID = os.getenv('CLIENT_ID')
Client_Secret = os.getenv('CLIENT_SECRET')

scope = os.getenv('SCOPES')


def get_access_token(client_id, client_secret, scope):
    url = 'https://iam.mcafee-cloud.com/iam/v1.1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'scope': scope,
        'audience': 'trellix'
    }
    auth = (client_id, client_secret)
    
    response = requests.post(url, headers=headers, data=data, auth=auth)
    
    if response.status_code == 200:
        #print(response.json().get('access_token'))
        return response.json().get('access_token')
    else:
        print(f"Error: {response.status_code}")
        return None


def insigths_events(api_key, access_token):
    url_base = 'https://api.manage.trellix.com/'
    resource = 'insights/v2/events'

    headers = {
        'Content-Type': 'application/vnd.api+json',
        'x-api-key': api_key,
        'Authorization': 'Bearer ' + access_token,
    }

    url = url_base + resource

    try:
        response = requests.get(url, headers=headers)
        data=response.json()
        pprint(data)
        return data
    except Exception as e:
        print("Erro ao fazer a solicitação GET: ")
        pprint(e)


def insigths_iocs(api_key, access_token):
    url_base = 'https://api.manage.trellix.com/'
    resource = 'insights/v2/iocs'

    headers = {
        'Content-Type': 'application/vnd.api+json',
        'x-api-key': api_key,
        'Authorization': 'Bearer ' + access_token,
    }

    url = url_base + resource

    try:
        response = requests.get(url, headers=headers)
        data=response.json()
        pprint(data)
        return data
    except Exception as e:
        print("Erro ao fazer a solicitação GET: ")
        pprint(e)


token = get_access_token(Client_ID, Client_Secret, SCOPES)

insigths_events(API_Key, token)
insigths_iocs(API_Key, token)
