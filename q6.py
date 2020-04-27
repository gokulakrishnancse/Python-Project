from github import Github
uname=input("Enter user name:")
username = uname
g = Github()
repo_name=input("Enter repository name(example:owner name/repository name):")
try:
    user = g.get_user(username)
    repo=g.get_repo(repo_name)
    print("Total number of stars in %s is %i"%(username,repo.stargazers_count))

except:
    print("Unable to find repository")
