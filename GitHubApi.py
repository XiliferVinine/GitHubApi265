import requests
import json

def gitHubReader(user):
    r = requests.get('https://api.github.com/users/%s/repos' % user)
    repositories = json.loads(r.content)
    for repository in repositories:
        numcommits = countCommits(repository['url'] + '/commits')
        repository['num_commits'] = numcommits
        print("Repo: " + repository['name'] + " Number of commits: " + str(numcommits))

def countCommits(commitsUrl):
    r = requests.get(commitsUrl)
    commits = json.loads(r.content)
    n = len(commits)
    return n

if __name__ == '__main__':
    print('Time to Retrieve!')
    gitHubReader('XiliferVinine')

