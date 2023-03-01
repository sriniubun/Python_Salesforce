import requests

# Replace with your Salesforce credentials
username = 'your_username'
password = 'your_password'
security_token = 'your_security_token'
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'

# Construct the authentication request payload
payload = {
    'grant_type': 'password',
    'client_id': consumer_key,
    'client_secret': consumer_secret,
    'username': username,
    'password': password + security_token
}

# Make a request to authenticate and get an access token
response = requests.post('https://login.salesforce.com/services/oauth2/token', data=payload)
access_token = response.json()['access_token']

# Make a request to the Salesforce API using the access token
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get('https://yourinstance.salesforce.com/services/data/v52.0/sobjects/Account', headers=headers)

# Print the response JSON
print(response.json())
