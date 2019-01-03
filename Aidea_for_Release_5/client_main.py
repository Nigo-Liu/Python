import json
import sys
from v2 import client


if __name__ == '__main__':

    # _argv_ip = sys.argv[1]
    # _argv_account = sys.argv[2]
    # _argv_password = sys.argv[3]
    
    client = client.Client('10.51.0.96', 'admin', 'admin')

    # print '====== List_Users =======' 

    # gu = client.users.get_users()
    # print gu
            
    # print '====== List_Projects ======='

    # lg = client.groups.list_groups('slurm')
    # print lg
    
    # print '====== List_Flavors ======='

    # f = client.flavors.list_flavors('slurm')
    # print f
       
    # print '====== Create_Job ======='

    # create_job_1 = client.jobs.create_job('slurm', 1, 'SLURM:SINGULARITY', 'docker://alpine:3.7', 1, 'aidea_demo_1', 'step-1', 'step-2', command_1='echo hello aidea_demo_1 >/aidea/test1.txt', path='/aidea', mountPath='/aidea', _type='HOSTPATH',  command_2='cat /aidea/test1.txt', schedule='', runs=1, dependency_policy='AFTEROK')
    # print create_job_1

    # create_job_2 = client.jobs.create_job('slurm', 1, 'SLURM:SINGULARITY', 'docker://alpine:3.7', 1, 'aidea_demo_2', 'step-1', 'step-2', command_1='echo hello aidea_demo_2 >/aidea/test2.txt', path='/aidea', mountPath='/aidea', _type='HOSTPATH',  command_2='cat /aidea/test2.txt', schedule='', runs=1, dependency_policy='AFTEROK')
    # print create_job_2

    # create_job_3 = client.jobs.create_job('slurm', 1, 'SLURM:SINGULARITY', 'docker://alpine:3.7', 1, 'aidea_demo_3', 'step-1', 'step-2', command_1='echo hello aidea_demo_3 >/aidea/test3.txt', path='/aidea', mountPath='/aidea', _type='HOSTPATH',  command_2='cat /aidea/test3.txt', schedule='', runs=1, dependency_policy='AFTEROK')
    # print create_job_3
    
    # print '====== List_Jobs ======='  
    
    # lj = client.jobs.list_jobs("slurm")
    # print lj

    print ('====== List_Jobs_Detail =======')
    ljd5 = client.jobs.get_job_detail("slurm", 5)
    print (ljd5)

    ljd6 = client.jobs.get_job_detail("slurm", 6)
    print (ljd6)

    ljd7 = client.jobs.get_job_detail("slurm", 7)
    print (ljd7)


    # print '====== Submit_Job ======='
    
    # sj4 = client.jobs.submit_job('slurm', 4, 'submit')
    # print sj4

    # sj5 = client.jobs.submit_job('slurm', 5, 'submit')
    # print sj5

    # sj6 = client.jobs.submit_job('slurm', 6, 'submit')
    # print sj6

    # sj7 = client.jobs.submit_job('slurm', 7, 'submit')
    # print sj7

    print ('====== Get_Job_runs =======')

    # gr3 = client.jobs.get_runs('slurm', 3)
    # print gr3

    # gr4 = client.jobs.get_runs('slurm', 4)
    # print gr4

    gr5 = client.jobs.get_runs('slurm', 5)
    print (gr5)

    gr6 = client.jobs.get_runs('slurm', 6)
    print (gr6)

    gr7 = client.jobs.get_runs('slurm', 7)
    print (gr7)

    print ('====== Get_logs =======')
    
    # gl = client.jobs.get_logs('slurm', 4, 2)
    # print gl  

    gl5_1 = client.jobs.get_logs('slurm', 5, 1)
    print (gl5_1)

    gl5_2 = client.jobs.get_logs('slurm', 5, 2)
    print (gl5_2)

    gl6_1 = client.jobs.get_logs('slurm', 6, 1)
    print (gl6_1)

    gl6_2 = client.jobs.get_logs('slurm', 6, 2)
    print (gl6_2)

    gl7_1 = client.jobs.get_logs('slurm', 7, 1)
    print (gl7_1)

    gl7_2 = client.jobs.get_logs('slurm', 7, 2)
    print (gl7_2)     

    # jd = client.jobs.get_job_detail('slurm', 2)
    # print jd

    # sj = client.jobs.submit_job('slurm', 3, 'stop')
    # print sj
    


    # lj = client.jobs.list_jobs()
    # print lj

