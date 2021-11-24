import requests

from plotly.graph_objs import Bar
from plotly import offline

# make API call and store the resonse.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names = [], []
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
