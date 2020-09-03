import tkinter as tk
#import docker
import os
from subprocess import check_output
import threading
from tkinter import *
import webbrowser
import time
import subprocess
from PIL import Image


# setting initial path at "/home/ubuntu/Desktop"
os.chdir("/home/ubuntu/Desktop")

window = tk.Tk()
window.title('LEADTEK')
window.geometry('800x350')
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

gdms_link = "" 
harbor_link = ""
netdata_link = ""

def deploy_components():
    global gdms_link
    global harbor_link
    global netdata_link

    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) :
        host_name = "gdms"
        host_list = check_output("virsh list --all | sed -n '3, 1p' | awk '{print $2}'", shell=True) 
        ip_address = ""
        if host_name not in host_list.decode('utf-8'):
            virsh_exec = ["/usr/bin/virt-install", "--virt-type", "kvm", "--name", "gdms",
                          "--vcpus=4", "--ram=8192", "--disk",
                          "/ssd/kvm/gdms_beta_v1.qcow2,format=qcow2,bus=virtio",
                          "--noautoconsole",
                          "--network", "bridge=br0", "--boot hd"]
            virsh_command = " ".join(virsh_exec)
            check_output(virsh_command, shell=True)
            mac_address = check_output("virsh domiflist gdms | awk '{print $5 }' | sed -n '3,1p'", shell=True).decode('utf-8')
            print (mac_address)
            str_mac = mac_address
            ip_exec = ["sudo", "arp-scan", "--interface=br0", "--localnet | grep ", str_mac.replace('\n',''), "| awk '{print $1}'"]
            ip_command = " ".join(ip_exec)
            ip_address = subprocess.check_output(ip_command, shell=True).decode('utf-8') 
            if ip_address == "":
                ip_address = subprocess.check_output(ip_command, shell=True).decode('utf-8')    
            elif ip_address.strip():
                return ip_address
            
            #i = 1
            #while i < 20:
                #i += 1
                #print (i)
                #str_mac = mac_address
                #ip_exec = ["sudo", "arp-scan", "--interface=br0", "--localnet | grep ", str_mac.replace('\n',''), "| awk '{print $1}'"]
                #ip_command = " ".join(ip_exec)
                #ip_address = subprocess.check_output(ip_command, shell=True).decode('utf-8')
                #print (ip_address)1
                #if ip_address.strip():
                    #break
                #return ip_address
        if ip_address == "":
            gdms_url = 'GDMS already installed on your RTX Package, plz check your kvm list.'
            label['text'] = gdms_url
        else:
            
            ipmsg = ip_address
            gdms_url = 'http://' + ipmsg + ':8080/GDMSWeb/'
            label['text'] = gdms_url
            gdms_link = gdms_url
    
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) :
        check_output('./deploy_harbor.sh', shell=True)
        harbor_url = 'https://rtxws.com:8443'
        label2['text'] = harbor_url
        harbor_link = harbor_url

    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) :
        check_output('./run_netdata.sh', shell=True)
        netdata_url = 'http://172.16.10.153:19999'
        label3['text'] = netdata_url
        netdata_link = netdata_url
    else:
        print("To do something.")

def delete_components():
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) :
        host_name = "gdms"
        host_list = check_output("virsh list | sed -n '3, 1p' | awk '{print $2}'", shell=True)
        if host_name in host_list.decode('utf-8'):
            check_output("virsh destroy gdms", shell=True)
            
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) :
        check_output('./deploy_harbor.sh', shell=True)
        harbor_url = 'https://rtxws.com:8443'
        label2['text'] = harbor_url
        harbor_link = harbor_url

    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) :
        check_output('./run_netdata.sh', shell=True)
        netdata_url = 'http://172.16.10.153:19999'
        label3['text'] = netdata_url
        netdata_link = netdata_url
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
        p = ""
        i = 1
        while i < 20: 
            i += 1
            p = check_output("./find_ip.sh").decode('utf-8')
            if p.strip():
                break
                return p
        ipmsg = p
        gdms_url = 'http://' + ipmsg + ':8080/GDMSWeb/'
        label_e1['text'] = gdms_url
        gdms_link = gdms_url

    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) :
        harbor_url = 'https://rtxws.com:8443'
        label_e3['text'] = harbor_url
        harbor_link = harbor_url

    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) :
        netdata_url = 'http://172.16.10.153:19999'
        label_e2['text'] = netdata_url
        netdata_link = netdata_url
    else:
        print("To do something.")
    
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

p_text = Text(window, width=22, height=3.1)
p_text.pack()
p_photo = PhotoImage(file="/home/ubuntu/leadtek.png")
p_text.image_create(END, image=p_photo)


c1 = tk.Checkbutton(window, text='GDMS', bg='white', variable=var1, onvalue=1, offvalue=0, command=deploy_seletcion)
c1.pack(anchor=NW)

c2 = tk.Checkbutton(window, text='Netdata', bg='white', variable=var2, onvalue=1, offvalue=0, command=deploy_seletcion)
c2.pack(anchor=W)

c3 = tk.Checkbutton(window, text='Harbor', bg='white', variable=var3, onvalue=1, offvalue=0, command=deploy_seletcion)
c3.pack(anchor=SW)

deploy_btn = tk.Button(window, text='DEPLOY', bg='white', command=lambda :thread_it(deploy_components)).pack(fill=X,anchor=S)
delete_btn = tk.Button(window, text='DELETE', bg='white', command=lambda :thread_it(delete_components)).pack(fill=X,anchor=S)

label = tk.Label(window) 
label.pack(fill=X,anchor=S)
label.bind("<Button-1>", lambda e: endpoint(gdms_link))

label3 = tk.Label(window)
label3.pack(fill=X,anchor=S)
label3.bind("<Button-1>", lambda e: endpoint_netdata(netdata_link))

label2 = tk.Label(window)
label2.pack(fill=X,anchor=S)
label2.bind("<Button-1>", lambda e: endpoint_harbor(harbor_link))

endpoint_btn = tk.Button(window, text='Endpoint', bg='white', command=lambda :thread_it(show_endpoint)).pack(fill=X,anchor=S)

label_e1 = tk.Label(window) 
label_e1.pack(fill=X,anchor=S)
label_e1.bind("<Button-1>", lambda e: endpoint(gdms_link))

label_e2 = tk.Label(window)
label_e2.pack(fill=X,anchor=S)
label_e2.bind("<Button-1>", lambda e: endpoint_netdata(netdata_link))

label_e3 = tk.Label(window)
label_e3.pack(fill=X,anchor=S)
label_e3.bind("<Button-1>", lambda e: endpoint_harbor(harbor_link))

window.mainloop()
