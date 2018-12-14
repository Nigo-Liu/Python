from gocloud.client.v2 import logs, categories, solutions, images, servers
from gocloud.client.v2 import groups, volumes, users
from gocloud.client.v2 import sites
from gocloud.client.v2 import snapshots
from gocloud.client.v2 import networks
from gocloud.client.v2 import lbs
from gocloud.client.v2 import registries
from gocloud.client.v2 import security_groups
from gocloud.client.v2 import infra
from gocloud.client.v2 import version
from gocloud.client.v2 import availability_zones
from gocloud.client.v2 import keypairs
from gocloud.client.v2 import notifications
from gocloud.client.v2 import flavors
from gocloud.client.v2 import jobs


class Client():
    def __init__(self, request, ip):
        self.users = users.Users(request, ip)
        self.logs = logs.Logs(request, ip)
        self.categories = categories.Categories(request, ip)
        self.solutions = solutions.Solutions(request, ip)
        self.images = images.Images(request, ip)
        self.servers = servers.Servers(request, ip)
        self.groups = groups.Groups(request, ip)
        self.volumes = volumes.Volumes(request, ip)
        self.sites = sites.Sites(request, ip)
        self.snapshots = snapshots.Snapshots(request, ip)
        self.networks = networks.Networks(request, ip)
        self.lbs = lbs.LoadBalancers(request, ip)
        self.flavors = flavors.Flavors(request, ip)
        self.security_groups = security_groups.Security_groups(request, ip)
        self.registries = registries.Registries(request, ip)
        self.infra = infra.Infra(request, ip)
        self.version = version.Version(request, ip)
        self.availability_zones =\
            availability_zones.AvailabilityZones(request, ip)
        self.keypairs = keypairs.Keypairs(request, ip)
        self.notifications = notifications.Notifications(request, ip)
        self.jobs = jobs.Jobs(request, ip)
