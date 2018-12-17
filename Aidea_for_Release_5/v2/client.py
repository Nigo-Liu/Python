from v2 import groups, users
from v2 import jobs
from v2 import flavors


class Client():
    def __init__(self, ip, account, password):
        self.users = users.Users(ip, account, password)
        self.groups = groups.Groups(ip, account, password)
        self.jobs = jobs.Jobs(ip, account, password)
        self.flavors = flavors.Flavors(ip, account, password)
