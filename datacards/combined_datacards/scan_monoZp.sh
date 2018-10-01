#!/bin/bash

samples_Zpdm=(DiJetsDM_MZprime-1000_Mhs-150_Mchi-10 DiJetsDM_MZprime-2000_Mhs-50_Mchi-10 DiJetsDM_MZprime-300_Mhs-50_Mchi-10 DiJetsDM_MZprime-500_Mhs-50_Mchi-10 DiJetsDM_MZprime-1000_Mhs-50_Mchi-10)

FS="Zpdm"

echo "med hs dm twosigdown onesigdown exp onesigup twosigup" > limits_${FS}.txt

for k in "${samples_Zpdm[@]}"; do
    branchingratio='1.0'

    cp boosted_resolved.txt combined.txt
    sed -i 's/XX-SIGNAL-XX/'${k}'/g' combined.txt
    
    #Computing limits
    combine -M Asymptotic -t -1 combined.txt --rAbsAcc 0 --rMax 30  | tee limits_tmp.txt
    #Parsing results into textfile
    #obs=`cat limits_tmp.txt | grep 'Observed Limit: r <' | awk '{print $5}'`
    twosigdown=`cat limits_tmp.txt | grep 'Expected  2.5%: r <' | awk '{print $5}'`
    onesigdown=`cat limits_tmp.txt | grep 'Expected 16.0%: r <' | awk '{print $5}'`
    exp=`cat limits_tmp.txt | grep 'Expected 50.0%: r <' | awk '{print $5}'`
    onesigup=`cat limits_tmp.txt | grep 'Expected 84.0%: r <' | awk '{print $5}'`
    twosigup=`cat limits_tmp.txt | grep 'Expected 97.5%: r <' | awk '{print $5}'`

    rm limits_tmp.txt

    #Applying branching ratio
    #obs=`echo "scale=7 ; $obs / $branchingratio" | bc`
    onesigdown=`echo "scale=7 ; $onesigdown / $branchingratio" | bc`
    twosigdown=`echo "scale=7 ; $twosigdown / $branchingratio" | bc`
    exp=`echo "scale=7 ; $exp / $branchingratio" | bc`
    onesigup=`echo "scale=7 ; $onesigup / $branchingratio" | bc`
    twosigup=`echo "scale=7 ; $twosigup / $branchingratio" | bc`

    echo "${k} ${twosigdown} ${onesigdown} ${exp} ${onesigup} ${twosigup}" >> limits_${FS}.txt

done
rm combined.txt
