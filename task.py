import requests
import getpass
import configparser


file_w = open("info.json", "w")
config = configparser.ConfigParser()
config.read("config.ini")
username = config['common']['username']
pull_url = config['common']['pull_url']
passwd = getpass.getpass()


def get_repo_info(uname, pwd):
    r = requests.get(pull_url, auth=(uname, pwd))
    out = r.json()
    file_w.write(str(out))
    print("State: %s " % str(out['state']))
    print("Title: %s " % str(out['title']))
    print("Merged: %s " % str(out['merged']))
    print("Commits: %s " % str(out['commits']))
    print("Repo name: %s " % str(out['head']['repo']['name']))
    print("Owner URL: %s " % str(out['base']['repo']['owner']['html_url']))


if __name__ == '__main__':
    get_repo_info(username, passwd)
