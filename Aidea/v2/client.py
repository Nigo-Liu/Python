from v2 import groups, users
from v2 import jobs
from v2 import flavors
from v2 import availability_zones


class Client():
    def __init__(self, ip, account, password):
        self.users = users.Users(ip, account, password)
        self.groups = groups.Groups(ip, account, password)
        self.jobs = jobs.Jobs(ip, account, password)
        self.flavors = flavors.Flavors(ip, account, password)
        self.availability_zones = availability_zones.AvailabilityZones(ip, account, password)