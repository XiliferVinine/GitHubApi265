import requests
import json

def gitHubReader(user):
    r = requests.get('https://api.github.com/users/%s/repos' % user)
    repositories = r.json()
    results = []
    for repository in repositories:
        repo_name = repository['name']
        cr = requests.get(repository['url'] + '/commits')
        commits = cr.json()
        numcommits = len(commits)
        results.append((repo_name, numcommits))
        repository['num_commits'] = numcommits
        print("Repo: " + repository['name'] + " Number of commits: " + str(repository['num_commits']))
    return(results)

# def countCommits(commitsUrl):
    # r = requests.get(commitsUrl)
    # commits = json.loads(r.content)
    # n = len(commits)
    # return n

if __name__ == '__main__':
    print('Time to Retrieve!')
    gitHubReader('XiliferVinine')


