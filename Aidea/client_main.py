import json
import sys
import api
from v2 import client


if __name__ == '__main__':
    
    _argv = sys.argv[1]   
    client = client.Client(_argv)
    
    

    # x = client.users.get_users()
    # print  
    y = client.jobs.list_jobs()
    print y

    # s = client.jobs.get_detail(2)
    # print s

    z = client.jobs.create_job(3, 'KUBERNETES:DOCKER', 'alpine:3.7', 17, 'post_test', 'sleep 60s')
    print z
