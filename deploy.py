import tkinter as tk
import docker
import os
from os import listdir
from subprocess import check_output, STDOUT
import threading
from tkinter import *
import webbrowser
import time
import subprocess
from PIL import Image

# setting initial path at "/home/ubuntu/Desktop"
os.chdir("/home/ubuntu/Desktop")

# tk GUI
window = tk.Tk()
window.title('LEADTEK')
window.geometry('800x600')
window.configure(background='white')

var = tk.StringVar()

l = tk.Label(window, bg='white', width=20, text='Deployment List')
l.pack()

def deploy_seletcion():
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) :
        l.config(text='Deploy GDMS ')
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) :
        l.config(text='Deploy Netdata')
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
        l.config(text='Deploy Harbor')
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0):
        l.config(text='Deployment List')
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0):
        l.config(text='Deploy GDMS & Netdata')
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1):
        l.config(text='Deploy GDMS & Harbor')
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1):
        l.config(text='Deploy Netdata & Harbor')
    else:
        l.config(text='Deploy all components')

client = docker.APIClient(base_url='unix://var/run/docker.sock')
gdms_link = "" 
harbor_link = ""
netdata_link = ""

def push_images():
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    os.chdir("/var/cache/images/")
    pull_info = tk.StringVar()
    for key,value in _varvalue.items():
        if value == 1:
            docker_exec = ["/usr/bin/docker", "load -i", key]
            docker_command = " ".join(docker_exec)
            check_output(docker_command, shell=True)
            t = 1
            while t < 30:
                image_list = check_output("docker images", shell=True).decode('utf-8')
                if str(key).replace('.tar','') in image_list:
                    print ('image upload completed')
                    for line in client.push('rtxws.com:8443/library/'+str(key).replace('.tar',''), stream=True):
                        print(line)
                        pull_info.set("image push completed.")
                    break
                else:
                    t += 1
    label4 = tk.Label(window, textvariable=pull_info, bg='white')
    label4.pack(fill=X,anchor=S)
def Readstatus(key):
    _var_obj = _var.get(key)
    print(_var_obj.get())
    _varvalue[key]=_var_obj.get()

def deploy_components():
    global gdms_link
    global harbor_link
    global netdata_link
    global _var
    global _varvalue
    # GDMS kvm deploy
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) :
        host_name = "gdms"
        host_list = check_output("virsh list --all | sed -n '3, 1p' | awk '{print $2}'", shell=True)
        if host_name not in host_list.decode('utf-8'):
            virsh_exec = ["/usr/bin/virt-install", "--virt-type", "kvm", "--name", "gdms",
                          "--vcpus=4", "--ram=8192", "--disk",
                          "/ssd/kvm/gdms_beta_v1.qcow2,format=qcow2,bus=virtio",
                          "--noautoconsole",
                          "--network", "bridge=br0", "--boot hd"]
            virsh_command = " ".join(virsh_exec)
            check_output(virsh_command, shell=True)
            mac_address = check_output("virsh domiflist gdms | awk '{print $5 }' | sed -n '3,1p'", shell=True).decode('utf-8')
            ip_exec = ["sudo", "arp-scan", "--interface=br0", "--localnet | grep ", mac_address.replace('\n',''), "| awk '{print $1}'"]
            ip_command = " ".join(ip_exec)
            t = 1
            while t < 8:
                ip_address = check_output(ip_command, shell=True, timeout=5).decode('utf-8') 
                if ip_address.strip():
                    break
                    return ip_address
                else:
                    t += 1
            if ip_address == "":
                gdms_link = 'Can`t get GDMS endpoint, please check your kvm configuration.'
                label['text'] = gdms_link
            else:
                gdms_link = 'http://' + ip_address.rstrip("\n") + ':8080/GDMSWeb/'
                label['text'] = gdms_link
        if host_name in host_list.decode('utf-8'):
            mac_address = check_output("virsh domiflist gdms | awk '{print $5 }' | sed -n '3,1p'", shell=True).decode('utf-8')
            ip_exec = ["sudo", "arp-scan", "--interface=br0", "--localnet | grep ", mac_address.replace('\n',''), "| awk '{print $1}'"]
            ip_command = " ".join(ip_exec)
            t = 1
            while t < 8:
                ip_address = check_output(ip_command, shell=True, timeout=5).decode('utf-8') 
                if ip_address.strip():
                    break
                    return ip_address
                else:
                    t += 1
            if ip_address == "":
                gdms_link = 'Can`t get GDMS endpoint, please check your kvm configuration.'
                label['text'] = gdms_link
            else:
                gdms_link = 'http://' + ip_address.rstrip("\n") + ':8080/GDMSWeb/'
                label['text'] = gdms_link
    # harbor deploy
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) :
        os.chdir("/home/ubuntu/harbor-master")
        harbor_list = check_output('sudo docker-compose ps', shell=True).decode('utf-8')
        harbor = "harbor"
        if harbor not in harbor_list:
            os.chdir("/home/ubuntu/harbor-master")
            check_output('sudo docker-compose up -d', shell=True)
            harbor_link = 'https://rtxws.com:8443'
            label3['text'] = harbor_link
            image_path = "/var/cache/images"
            image_list = listdir(image_path)
            _var = dict()
            _varvalue = dict()
            # dynamic create image tar file to checkbutton
            for image in image_list:
                _var[image] = tk.IntVar()
                _varvalue[image] = 0
                image = tk.Checkbutton(window, text=image, bg='white', variable=_var[image], onvalue=1, offvalue=0, command=lambda key=image: Readstatus(key))
                image.pack(anchor=NW) 
            # create push_image button
            push_btn = tk.Button(window, text='Push_images', bg='white', command=lambda :thread_it(push_images)).pack(fill=X,anchor=S)
        elif harbor in harbor_list:
            harbor_link = 'https://rtxws.com:8443'
            label3['text'] = harbor_link
            image_path = "/var/cache/images"
            image_list = listdir(image_path)
            _var = dict()
            _varvalue = dict()
            # dynamic create image tar file to checkbutton
            for image in image_list:
                _var[image] = tk.IntVar()
                _varvalue[image] = 0
                print(type(tk.IntVar()))
                print(type(_var[image]))
                image = tk.Checkbutton(window, text=image, bg='white', variable=_var[image], onvalue=1, offvalue=0, command=lambda key=image: Readstatus(key))
                image.pack(anchor=NW)
            # create push_image button
            push_btn = tk.Button(window, text='Push_images', bg='white', command=lambda :thread_it(push_images)).pack(fill=X,anchor=S)
    # netdata(gpu & system monitor tool
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) :
        check_output('./run_netdata.sh', shell=True)
        netdata_link = 'http://172.16.10.153:19999'
        label2['text'] = netdata_link
    else:
        print("To do something.")

def delete_components():
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) :
        host_name = "gdms"
        host_list = check_output("virsh list | sed -n '3, 1p' | awk '{print $2}'", shell=True)
        if host_name in host_list.decode('utf-8'):
            check_output("virsh destroy gdms", shell=True)
            gdms_link = 'GDMS removed.'
            label['text'] = gdms_link
        else:
            gdms_link = 'GDMS doesn`t installed.'
            label['text'] = gdms_link            
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) :
        os.chdir("/home/ubuntu/harbor-master")
        harbor_list = check_output('sudo docker-compose ps', shell=True).decode('utf-8')
        harbor = "harbor"
        if harbor in harbor_list:
            os.chdir("/home/ubuntu/harbor-master")
            check_output('sudo docker-compose down -v', shell=True)
            harbor_link = 'harbor removed.'
            label3['text'] = harbor_link
        else:
            harbor_link = 'harbor doesn`t installed.'
            label3['text'] = harbor_link
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) :
        check_output('./run_netdata.sh', shell=True)
        netdata_link = 'http://172.16.10.153:19999'
        label2['text'] = netdata_link
    else:
        print("To do something.")

def endpoint(url):
    webbrowser.open_new(url)

def endpoint_harbor(url):
    subprocess.call("xdg-open "+ url, shell=True)    

def endpoint_netdata(url):
    webbrowser.open_new(url)

def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()

def show_endpoint():
    global gdms_link
    global harbor_link
    global netdata_link    
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) :
        mac_address = check_output("virsh domiflist gdms | awk '{print $5 }' | sed -n '3,1p'", shell=True).decode('utf-8')
        ip_exec = ["sudo", "arp-scan", "--interface=br0", "--localnet | grep ", mac_address.replace('\n',''), "| awk '{print $1}'"]
        ip_command = " ".join(ip_exec)
        t = 1
        while t < 8:
            ip_address = check_output(ip_command, shell=True, timeout=5).decode('utf-8') 
            if ip_address.strip():
                break
                return ip_address
            else:
                t += 1
        if ip_address == "":
            gdms_link = 'Can`t get GDMS endpoint, please check your kvm configuration.'
            label['text'] = gdms_link
        else:
            gdms_link = 'http://' + ip_address.rstrip("\n") + ':8080/GDMSWeb/'
            label['text'] = gdms_link
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) :
        os.chdir("/home/ubuntu/harbor-master")
        docker_list = check_output('sudo docker-compose ps', shell=True).decode('utf-8')
        print(docker_list)
        harbor_link = 'https://rtxws.com:8443'
        label3['text'] = harbor_link
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) :
        netdata_link = 'http://172.16.10.153:19999'
        label2['text'] = netdata_link
    else:
        print("To do something.")
def show_images():
    global _var
    global _varvalue
    harbor_link = 'https://rtxws.com:8443'
    label3['text'] = harbor_link
    image_path = "/var/cache/images"
    image_list = listdir(image_path)
    _var = dict()
    _varvalue = dict()
    # dynamic create image tar file to checkbutton
    for image in image_list:
        _var[image] = tk.IntVar()
        _varvalue[image] = 0
        image = tk.Checkbutton(window, text=image, bg='white', variable=_var[image], onvalue=1, offvalue=0, command=lambda key=image: Readstatus(key))
        image.pack(anchor=NW)
    # create push_image button
    push_btn = tk.Button(window, text='Push_images', bg='white', command=lambda :thread_it(push_images)).pack(fill=X,anchor=S)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

#LEADTEK Logo
p_text = Text(window, width=22, height=3.1)
p_text.pack()
p_photo = PhotoImage(file="/home/ubuntu/leadtek.png")
p_text.image_create(END, image=p_photo)

#CheckBox
c1 = tk.Checkbutton(window, text='GDMS', bg='white', variable=var1, onvalue=1, offvalue=0, command=deploy_seletcion)
c1.pack(anchor=NW)
c2 = tk.Checkbutton(window, text='Netdata', bg='white', variable=var2, onvalue=1, offvalue=0, command=deploy_seletcion)
c2.pack(anchor=W)
c3 = tk.Checkbutton(window, text='Harbor', bg='white', variable=var3, onvalue=1, offvalue=0, command=deploy_seletcion)
c3.pack(anchor=SW)

#Button
deploy_btn = tk.Button(window, text='DEPLOY', bg='white', command=lambda :thread_it(deploy_components)).pack(fill=X,anchor=S)
delete_btn = tk.Button(window, text='DELETE', bg='white', command=lambda :thread_it(delete_components)).pack(fill=X,anchor=S)
endpoint_btn = tk.Button(window, text='Endpoint', bg='white', command=lambda :thread_it(show_endpoint)).pack(fill=X,anchor=S)
showimages_btn = tk.Button(window, text='Docker_images_list', bg='white', command=lambda :thread_it(show_images)).pack(fill=X,anchor=S)

#Display_Label
label = tk.Label(window, bg='white') 
label.pack(fill=X,anchor=S)
label.bind("<Button-1>", lambda e: endpoint(gdms_link))

label2 = tk.Label(window, bg='white')
label2.pack(fill=X,anchor=S)
label2.bind("<Button-1>", lambda e: endpoint_netdata(netdata_link))

label3 = tk.Label(window, bg='white')
label3.pack(fill=X,anchor=S)
label3.bind("<Button-1>", lambda e: endpoint_harbor(harbor_link))

window.mainloop()
