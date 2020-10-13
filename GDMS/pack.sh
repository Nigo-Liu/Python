#!/bin/sh
read -p "Input a tar file path : " file
read -p "Input a run file path : " run

# is file exsted >
if [ ! -f ${file} ]
then
    echo "no such file"
    exit 1
fi
# check file extension
extension=$(basename ${file} | tr "[:upper:]" "[:lower:]" | tr '.' '\n' | tail -n 1)
if [ ${extension} != "tar" ]
then
    echo "only support tar file"
    exit 1
fi
echo "packing...."
#sudo /bin/sh -c  'echo "PAYLOAD:" >> $run'
sudo echo "PAYLOAD:" >> "$run"
# append tar file
cat ${file} | sudo tee -a "$run" > /dev/null
echo "done"
