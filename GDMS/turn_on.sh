#!/bin/bash

LOGFILE=/var/log/gdms_deployment.log

fun_date()
{
    while IFS= read -r line; do
    printf '%s %s\n' "$(date)" "$line";
    done
}

fun_get_ip()
{
    i=1
    while [ $i -le 100 ]
    do
      host_name=$(virsh list | sed -n "3, 1p" | awk '{print $2}')
      echo "Get a hostname : $host_name"
      mac_address=$(virsh domiflist "$host_name" | awk '{print $5 }' | sed -n "3,1p")
      echo "Get a mac address : $mac_address"
      ip=$(sudo arp-scan --interface=br0 --localnet | grep "$mac_address" | awk '{print $1}')
      echo "Get a GDMS endpoint : $ip"
      if [ -n "$ip" ]
      then
        sudo echo "GDMS endpoint : http://$ip:8080/GDMSWeb/" > /home/ubuntu/Desktop/GDMS_Endpoint
	break
      fi
      i=$(( $i+1 ))
      sleep 2
      echo "Retry to get a GDMS endpoint..."
    done
    if [ -z "$ip" ]
    then
      echo "GDMS turn on filed." > /home/ubuntu/Desktop/GDMS_Endpoint
    fi  
}

fun_turn_on_gdms()
{
    echo "Turn on GDMS..."
    virsh_list=$(virsh list --all | sed -n '3, 1p' | awk '{print $2}')
    echo $virsh_list
    if [ "$virsh_list" = "gdms" ]
    then
        echo "The GDMS was already turned on."
    else
        sudo virt-install --virt-type kvm --name gdms \
        --vcpus=4 --ram=8192 --autostart \
        --disk /var/lib/libvirt/images/gdms_v1.img,format=raw,bus=virtio \
        --noautoconsole --network bridge=br0 --boot hd &
        echo "Waiting for GDMS..."
        sleep 10
        echo "The GDMS has been created successfully."
    fi
}

deploy()
{
    fun_turn_on_gdms
    fun_get_ip
}

deploy 2>&1 | fun_date | sudo tee -a $LOGFILE
#sudo sed -i "/get_ip/d" /etc/rc.local
sudo sed -i "/turn_on/d" /etc/rc.local
exit 0
