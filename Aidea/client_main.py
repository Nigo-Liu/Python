import json
import sys
from v2 import client
import getopt
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type = str, help = 'Your API Server IP.')
    parser.add_argument('-u', '--account', type = str, help = 'Your account name.')
    parser.add_argument('-p', '--password', type = str, help = 'Your acconut password.')
    parser.add_argument('-f', '--function', type = int, choices=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], default = 1, help = 'choices your API function. [1: list_users] [2: list_projects] [3: list_jobs] [4: create_job] [5: submit_job] [6: create_job_volume] [7: stop_job] [8: list_job_detail] [9: list_flavors] [10: create_user] [11: delete_user] [12: list_availability_zones][13: get job runs]' )
    parser.add_argument('-project_id', '--project_id', type = str, default='1', help = 'Your project id for create job' )
    parser.add_argument('-job_type', '--job_type', type = str, default = 'KUBERNETES:DOCKER', help = 'Your job_type, default is KUBERNETES:DOCKER for create job' )
    parser.add_argument('-image_name', '--image_name', type = str, default = 'alpine:3.7', help = 'Your docker image name. default is alpine:3.7 for create job.' )
    parser.add_argument('-flavor_id', '--flavor_id', type = str, default='17', help = 'Your flavor id for create job.' )
    parser.add_argument('-job_name', '--job_name', type = str, default = 'test_job', help = 'Your job name for create job.' )
    parser.add_argument('-command', '--command', type = str, default = 'sleep 60s', help = 'Your command line for create job.' )
    parser.add_argument('-job_id', '--job_id', type = str, default = '1', help = 'Your job id for list and submit job.' )
    parser.add_argument('-server', '--server', type = str, default = '127.0.0.1', help = 'Your volume server ip for create job.' )
    parser.add_argument('-location', '--location', type = str, default = 'text', help = 'Your volume location for create job.' )
    parser.add_argument('-mountPath', '--mountPath', type = str, default = '/test/volume/', help = 'Your volume mountPath for create job.' )
    parser.add_argument('-user_name', '--user_name', type = str, default = 'test', help = 'Your account for create user.' )
    parser.add_argument('-user_password', '--user_password', type = str, default = 'password', help = 'Your account password for create user.' )
    parser.add_argument('-user_email', '--user_email', type = str, default = 'email', help = 'Your email address for create user.' )
    parser.add_argument('-user_id', '--user_id', type = str, default = '1', help = 'Your user id for delete user.' )
    parser.add_argument('-schedule', '--schedule', type = str, default = '', help = 'Your schedule for create job.')

    args = parser.parse_args()
    
    if args.function == 1:
        print ('=========list users=========')
        client = client.Client(args.ip, args.account, args.password)
        gu = client.users.get_users()
        print (gu)     
    
    if args.function == 2:
        print ('=========list projects=========')
        client = client.Client(args.ip, args.account, args.password)
        lg = client.groups.list_groups()
        print (lg) 

    if args.function == 3:
        print ('=========list jobs=========')
        client = client.Client(args.ip, args.account, args.password)
        lj = client.jobs.list_jobs()
        print (lj)           

    if args.function == 4:
        print ('=========create job=========')
        client = client.Client(args.ip, args.account, args.password)
        cj = client.jobs.create_job(args.project_id, args.job_type, args.image_name, args.flavor_id, args.job_name, args.command, args.schedule)
        print (cj)        

    if args.function == 5:
        print ('=========submit job=========')
        client = client.Client(args.ip, args.account, args.password)
        sj = client.jobs.submit_job(args.job_id, 'submit')    
        print (sj)

    if args.function == 6:
        print ('=========create job=========')
        client = client.Client(args.ip, args.account, args.password)
        cj = client.jobs.create_job_volume(args.project_id, args.job_type, args.image_name, args.flavor_id, args.job_name, args.command, args.server, args.location, args.mountPath)
        print (cj)

    if args.function == 7:
        print ('=========stop job=========')
        client = client.Client(args.ip, args.account, args.password)
        sj = client.jobs.submit_job(args.job_id, 'stop')    
        print (sj)

    if args.function == 8:
        print ('=========get job detail=========')
        client = client.Client(args.ip, args.account, args.password)
        jd = client.jobs.get_job_detail(args.job_id)
        print (jd)

    if args.function == 9:
        print ('=========list flavor=========')
        client = client.Client(args.ip, args.account, args.password)
        f = client.flavors.list_flavors()
        print (f)

    if args.function == 10:
        print ('=========create_user=========')
        client = client.Client(args.ip, args.account, args.password)
        cu = client.users.create_users(args.user_name, args.user_password, args.user_email)
        print (cu)

    if args.function == 11:
        print ('=========delete_user=========')
        client = client.Client(args.ip, args.account, args.password)
        du = client.users.delete_users(args.user_id)
        print (du)

    if args.function == 12:
        print ('=========list_availability_zones=========')
        client = client.Client(args.ip, args.account, args.password)
        az = client.availability_zones.list_azs()
        print (az)

    if args.function == 13:
        print ('=========get_job_runs=========')
        client = client.Client(args.ip, args.account, args.password)
        gr = client.jobs.get_runs(args.job_id)
        print (gr)

    # print '====== Project ======='

    # cg = client.groups.create_group('Aidea_2')
    # print cg

    # lg = client.groups.list_groups()
    # print lg
 
    # gd = client.groups.get_detail(4)
    # print gd 

    # print '====== User =======' 

    # cu = client.users.create_users('nigo_test_2', 'password', 'nigo@gemini.com')

    # gu = client.users.get_users()
    # print gu
    
    # a = client.users.associate(3, 4)
        
    # print '====== Flavor ======='

    # f = client.flavors.list_flavors()
    # print f

    # print '====== Job ======='

    # cj = client.jobs.create_job(3, 'KUBERNETES:DOCKER', 'alpine:3.7', 17, 'post_test_13', 'sleep 60s')
    # print cj

    # lj = client.jobs.list_jobs()
    # print lj

    # jd = client.jobs.get_job_detail(8)
    # print jd

    # sj = client.jobs.submit_job(9, 'submit')
    # print sj

    # lj = client.jobs.list_jobs()
    # print lj

