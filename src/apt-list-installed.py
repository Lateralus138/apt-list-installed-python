#!/usr/bin/env python3
import sys 
import os.path
from subprocess import call
helpMsg = '''
Usage: apt-get-installed [-h,--help]
Usage <Python>: python3 apt-get-installed.py [-h,--help]

 -h, --help		This help message

Retrieve a simple list of applications installed with
the apt package management system.

apt-list-installed is dependent on Bash.
'''
if len(sys.argv) > 1:
	if sys.argv[1] in ["-h","--help"]:
		print(helpMsg)
	quit()
if os.path.isfile("/bin/bash"):
	shell="/bin/bash"
else:
	print(sys.argv[0] +  " is dependent on Bash and Bash could not be found at /bin/bash.")
	quit()
com = '''\
readarray array <<< $(apt list 2>/dev/null | grep "\[installed")
for ((idx=0;idx<"${#array[@]}";idx++)); do
	array[$idx]="${array[$idx]//$'\n'/}"
	array[$idx]="${array[$idx]%\/*}"
done
for installed in ${array[@]}; do
	echo "${installed}"
done\
'''
call([shell,"-c",com])
