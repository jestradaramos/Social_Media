#!/bin/bash
## Author: Jeffrey Estrada

# First get all the authentication that is needed
# Email : Gmail with PWD

GMAIL=`sed -n '1p' < keys.txt | cut -d ":" -f 2`
PWD=`sed -n '2p' < keys.txt | cut -d ":" -f 2`
echo $GMAIL
echo $PWD

# FB: API Keys + Group ID

FBK=`sed -n '3p' < keys.txt | cut -d ":" -f 2`
FBI=`sed -n '4p' < keys.txt | cut -d ":" -f 2`
echo $FBK
echo $FBI

# Twitter: App Key and App Secret Key

TAK=`sed -n '5p' < keys.txt | cut -d ":" -f 2`
TSK=`sed -n '6p' < keys.txt | cut -d ":" -f 2`
echo $TAK
echo $TSK

