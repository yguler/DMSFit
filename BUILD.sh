#!/bin/bash

set -e 

#for i in boosted_mass0 boosted_mass1 boosted_mass2 boosted_mass3
#for i in boosted_mass0_subjet boosted_mass1_subjet boosted_mass2_subjet boosted_mass3_subjet
#for i in boosted_mass0_subjet_2017 boosted_mass1_subjet_2017 boosted_mass2_subjet_2017 boosted_mass3_subjet_2017

#for i in boosted_mass0f boosted_mass0p boosted_mass1f boosted_mass1p boosted_mass2f boosted_mass2p boosted_mass3f boosted_mass3p
#do
#    python buildModel.py $i
#done

#rm mono-x.root

hadd mono-x.root mono-x0p.root mono-x1p.root mono-x2p.root mono-x3p.root mono-x0f.root mono-x1f.root mono-x2f.root mono-x3f.root

if [ -e mono-x.root ];then
    python runModel_boosted.py
else
    exit 0
fi
