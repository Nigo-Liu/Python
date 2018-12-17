import json
import sys
import api
from v2 import client


if __name__ == '__main__':
    
    _argv_ip = sys.argv[1]
    _argv_account = sys.argv[2]
    _argv_password = sys.argv[3]
  
    client = client.Client(_argv_ip, _argv_account, _argv_password)


    print '====== Project ======='

    # cg = client.groups.create_group('Aidea_2')
    # print cg

    # lg = client.groups.list_groups()
    # print lg
 
    # gd = client.groups.get_detail(4)
    # print gd 

    print '====== User =======' 

    # cu = client.users.create_users('nigo_test_2', 'password', 'nigo@gemini.com')

    # gu = client.users.get_users()
    # print gu
    
    # a = client.users.associate(3, 4)
        
    print '====== Flavor ======='

    # f = client.flavors.list_flavors()
    # print f

    print '====== Job ======='

    # cj = client.jobs.create_job(3, 'KUBERNETES:DOCKER', 'alpine:3.7', 17, 'post_test_13', 'sleep 60s')
    # print cj

    lj = client.jobs.list_jobs("slurm")
    print lj

    # jd = client.jobs.get_job_detail(8)
    # print jd

    # sj = client.jobs.submit_job(9, 'submit')
    # print sj

    # lj = client.jobs.list_jobs()
    # print lj

