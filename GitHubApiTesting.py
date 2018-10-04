
import json
import unittest
from unittest.mock import patch, Mock
from nose.tools import assert_equal

from GitHubApi import gitHubReader
# from GitHubApi import countCommits

class TestGitHubApi(unittest.TestCase):

    @patch('requests.get')
    def test_num_commits(injectedMock):
        commit_count = gitHubReader('XiliferVinine')
        results = [Mock(), Mock(), Mock()]
        results[0].json.return_value = json.loads('[ { "name" : "GitHubApi265" },  { "name" : "Triangle265" } ]')
        results[1].json.return_value = json.loads('[ { "commit" : "blah" }, { "commit" : "blue" }, { "commit" : "derp" }, { "commit" : "some" }, { "commit" : "dang" } ]')
        results[2].json.return_value = json.loads('[ { "commit" : "fork" }, { "commit" : "knife" }, { "commit" : "spoon" }, { "commit" : "plate" } ]')
        injectedMock.side_effect = results
        assert_equal(commit_count, [('GitHubApi265', 5), ('Triangle265', 4)])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()