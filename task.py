import requests
import getpass
import argparse

parser = argparse.ArgumentParser(prog="Task")
parser.add_argument('username', help="Name of user")
parser.add_argument('prurl', help="URL of PR")
parser.add_argument('--state', '-s', action="store_true", help="Show state of PR")
parser.add_argument('--title', '-t', action="store_true", help="Show title")
parser.add_argument('--merged', '-m', action="store_true", help="Show merge state")
parser.add_argument('--commits', '-c', action="store_true", help="Show commits count")
parser.add_argument('--reponame', '-r', action="store_true", help="Show name of repo")
parser.add_argument('--ownerurl', '-o', action="store_true", help="Show owner URL")
passwd = getpass.getpass()
args = parser.parse_args()
username = args.username
pull_url = args.prurl


def get_repo_info(uname, pwd):
    r = requests.get(pull_url, auth=(uname, pwd)).json()
    if args.state:
        print("State: %s " % r['state'])
    if args.title:
        print("Title: %s " % str(r['title']))
    if args.merged:
        print("Merged: %s " % str(r['merged']))
    if args.commits:
        print("Commits: %s " % str(r['commits']))
    if args.reponame:
        print("Repo name: %s " % r['head']['repo']['name'])
    if args.ownerurl:
        print("Owner URL: %s " % r['base']['repo']['owner']['html_url'])


if __name__ == '__main__':
    get_repo_info(username, passwd)
