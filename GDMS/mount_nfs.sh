#!/bin/bash

LOGFILE=/var/log/gdms_mount_nfs.log
#LOGFILE=/var/log/gdms_deployment.log
nfsip="rtxip"

fun_date()
{
    while IFS= read -r line; do
    printf '%s %s\n' "$(date)" "$line";
    done
}

fun_mount_nfs()
{
  set -x 
  echo "Waiting for get a GDMS IP..."
  i=1
  while [ $i -le 200 ]
  do
    ip=$(sudo ifconfig eth0 | grep -w inet | awk -F ":" '{print $2}' | awk '{print $1}')
    if [ -n "$ip" ]
    then
      echo "GDMS IP : $ip"
      echo "Web service stop..."
      sudo service tomcat6 stop
      sudo service apache2 stop
      echo "Backup GdmsData folder..."
#      sudo rsync -avhP /dms/dat/GdmsData /home/dms-adm/
      sudo mv /dms/dat/GdmsData /home/dms-adm/
      echo "Check NFS Server IP..."
      echo "The NFS Server IP : $nfsip"
      echo "Mount nfs server... "
      sudo mount $nfsip:/dat /dms/dat
      echo "Automatically mounting NFS with /etc/fstab"
      sudo sed -i "/none/a $nfsip:/dat /dms/dat nfs defaults 0 0" /etc/fstab
      echo "Restore GdmsData folder..."
      sudo rsync -avhP /home/dms-adm/GdmsData /dms/dat/
#      sudo mv /home/dms-adm/GdmsData /dms/dat/
      echo "Restart samba and vsftp service..."
      sudo service samba restart
      sudo service vsftpd restart
      sudo service tftpd-hpa restart
      echo "Web service start..."
      sudo service apache2 start
      sudo service tomcat6 start
      break
    fi
    i=$(( $i+1 ))
    sleep 2
    echo "Retry to get a GDMS IP..."
  done
  if [ -z "$ip" ]
  then
    echo "GDMS get IP filed."
  fi
}

fun_mount_nfs | fun_date | sudo tee -a $LOGFILE
sudo sed -i "/mount_nfs/d" /etc/rc.local
