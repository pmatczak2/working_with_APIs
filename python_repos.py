import requests

# make API call and store the resonse.
url = 'https://api.github.com/search/repositories?q=launguage:python$sort=start'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Process results.
print(response_dict.keys())