# Social Media

The main purpose of this repo is to contain any scripts that may be useful for 
automating tasks, such as posting on social media and sending emails.

## Necessary Libraries
Most of this script is written in python, therfore there are some libraries that
are going to be needed to install before using this script. Keep in mind that 
this script is using python3, so install the proper libraries. 

### Libraries Used
- facepy
```pip3 install facepy```
- twython
```pip3 install twython```

## Setting Up
There is going to be some set up needed before using this script. This script uses
facebook, twitter, and gmail api in order to send out your message on all 3 platform.
That means that we are going to need to generate access tokens and set the right 
permissions to get this up and running. 

1) In this repo you will find a file called ```mykeys_Template```. What you are going 
to want to do is rename that file to ```mykeys```. And inside that file you will find
some sections. Fill in the appropriate elements in each section. 
2) GMAIL and PWD are for your email and password for a gmail account in order to 
actually send emails via SMTP.
3)FB_KEY is the key you get from facebook in order to use their api. And Group ID is 
ID of the facebook group that you want to post to. You can use online tools to find 
the group ID of the page you want to  post to. 
4) TW_KEY and TW_S_KEY are the keys provided by twitter in order to access their API.
