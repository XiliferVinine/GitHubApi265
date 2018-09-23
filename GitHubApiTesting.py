

import unittest

from GitHubApi import gitHubReader
from GitHubApi import countCommits

class TestGitHubApi(unittest.TestCase):

    def testNumCommits(self):
        self.assertEqual(countCommits('https://api.github.com/repos/XiliferVinine/SSW555-GEDCOM/commits'), 25, 25)
        self.assertEqual(countCommits('https://api.github.com/repos/XiliferVinine/Test-Survey-System/commits'), 30, 30)
        self.assertEqual(countCommits('https://api.github.com/repos/XiliferVinine/Triangle265/commits'), 6, 6)
        self.assertEqual(countCommits('https://api.github.com/repos/XiliferVinine/Hw-00-tools-setup/commits'), 3, 3)
        self.assertEqual(countCommits('https://api.github.com/repos/XiliferVinine/GitHubApi265/commits'), 5, 5)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()