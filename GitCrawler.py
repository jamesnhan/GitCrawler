import requests
import json
import time

start = time.time()

count = 0

result = requests.get('https://api.github.com/search/repositories?q=a&sort=stars&order=desc')
jsondict = json.loads(result.text)
for project in jsondict['items']:
    print(project['full_name'] + ' by ' + project['owner']['login'])
    print('\t Stars: \t' + str(project['stargazers_count']))
    print('\t Watchers: \t' + str(project['watchers_count']))
    print('\t Forks: \t' + str(project['forks_count']))
    print('\t Open Issues: \t' + str(project['open_issues_count']))
    count = count + 1

end = time.time()

print('Time Taken: ' + str(end - start))
print('Count: ' + str(count))
