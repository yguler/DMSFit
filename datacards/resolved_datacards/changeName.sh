#!/bin/bash

for bin in mass0 mass1 mass2 mass3
do
    eval cd ${bin}
    for i in `ls resolved_*.txt`
    do
	echo "sed -e s/..\/..\/..\/combined_model_resolved.root/..\/..\/combined_model_resolved.root/g $i > temp"
	sed -e "s/resolved_pass_mass0_fail/resolved_fail_mass0/g" $i > temp
	mv temp $i
    done
    eval cd ..
done