#!/bin/bash
readarray array <<< $(apt list 2>/dev/null | grep "\[installed")
for ((idx=0;idx<"${#array[@]}";idx++)); do
	array[$idx]="${array[$idx]//$'\n'/}"
	array[$idx]="${array[$idx]%\/*}"
done
echo -e "\e[1;91mInstalled Packages: ${#array[@]}\e[0m"
for name in "${array[@]}"; do
	echo -e "\e[1;92m${name}\e[0m"
done
#echo -e "\e[1;91mInstalled Packages: \e[1;93m${#array[@]}\e[0m"
for installed in ${array[@]}; do
	echo "${installed}"
done\
