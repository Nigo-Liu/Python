from v2 import groups, users
from v2 import jobs
from v2 import flavors


class Client():
    def __init__(self, ip):
        self.users = users.Users(ip)
        self.groups = groups.Groups(ip)
        self.jobs = jobs.Jobs(ip)
        self.flavors = flavors.Flavors(ip)
