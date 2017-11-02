#!/bin/bash
## Author: Jeffrey Estrada

# First get all the authentication that is needed
# Email : Gmail with PWD
GMAIL=`sed -n '1p' < mykeys | cut -d ":" -f 2`
PWD=`sed -n '2p' < mykeys | cut -d ":" -f 2`
EMAIL="jestrada@wpi.edu"

# FB: API Keys + Group ID
FBK=`sed -n '3p' < mykeys | cut -d ":" -f 2`
FBI=`sed -n '4p' < mykeys | cut -d ":" -f 2`

# Twitter: App Key and App Secret Key
TAK=`sed -n '5p' < mykeys | cut -d ":" -f 2`
TSK=`sed -n '6p' < mykeys | cut -d ":" -f 2`


echo $GMAIL
echo $PWD
echo $FBK
echo $FBI
echo $TAK
echo $TSK

# This only needs to be done once
#python3 auth_tweet.py $TAK $TSK

TAT=`sed -n '7p' < mykeys | cut -d ":" -f 2`
TAS=`sed -n '8p' < mykeys | cut -d ":" -f 2`

echo $TAT
echo $TAS

echo Enter Subject:
echo Press Ctrl + d to finish
cat - > sub


echo Enter Message:
echo Press Ctrl + d to finish

cat - > msg


echo Enter tweet:
echo Press Ctrl + d to finish

cat - > tweet

# Send Email
python3 gmail.py $GMAIL $PWD $EMAIL sub msg

# Send FB

python3 fb.py $FBK $FBI test2

# Send tweet
python3 tweet.py $TAK $TSK $TAT $TAS tweet 

rm sub
rm msg
rm tweet
