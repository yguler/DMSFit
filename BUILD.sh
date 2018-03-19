#!/bin/bash

set -e 

for i in boosted_mass0 boosted_mass1 boosted_mass2 boosted_mass3
do
    python buildModel.py $i
done

if [-e mono-x.root];then
    rm mono-x.root
fi

hadd mono-x.root boosted-mass0.root boosted-mass1.root boosted-mass2.root boosted-mass3.root

if [ -e mono-x.root ];then
    python runModel_boosted.py
else
    exit 0
fi
