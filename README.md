![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)

# TuTu Twitter ThreadSaver
Helps to Save Twiiter Thread by Tagging/Mentioning us. Under any Tweet you want to save, reply by mentioning our bot @binilchengankal. Wait for a minute for the reply from bot. A reply will be sent as direct message (⚠️ bot won't run unless you follow bot - As Twiiter policy is restricting bot to do so). Kindly make sure to follow bot before mentioning/tagging us.Thank you

## Team members

1. [Abhijith KJ](https://github.com/abhijith666)
2. [Akhil Shalil](https://github.com/akku127)

## Team Id

BFH/recqA2DMkbksFm0hb/2021

## Link to product walkthrough

[Link to Video](https://www.loom.com/share/0ccfe2e34dc94da1ab6bf09e1801a5e3)

[![](https://cdn.loom.com/sessions/thumbnails/0ccfe2e34dc94da1ab6bf09e1801a5e3-with-play.gif)](https://www.loom.com/share/0ccfe2e34dc94da1ab6bf09e1801a5e3)

## How it Works ?

Bot uses tweepy to get the tweets where the bot is Tagged/Mentioned.
From the it collect recipent ID, Tweet ID, Tweet Text and URL.Bot uses twitter API to send direct Message to the Recipent.

[Demo Video](https://www.loom.com/share/0ccfe2e34dc94da1ab6bf09e1801a5e3)

[![](https://cdn.loom.com/sessions/thumbnails/de6860cf4bbc4f0db0848d9f6e0285ad-1621800829799-with-play.gif)](https://www.loom.com/share/de6860cf4bbc4f0db0848d9f6e0285ad)

## Libraries used

TwitterAPI
tweepy

## How to configure

# How To Install? & How To Use? :

## To Test Bot without Installing

### \>\> Login to [Twitter](https://www.twiiter.com/)

### \>\> ⚠️ Follow [Bot](https://twitter.com/binilchengankal) On [Twitter](https://www.twiiter.com/)

!!! Thread Saver Wont Work Unless You Follow Bot !!!

### \>\> Reply under any Tweet by mentioning Bot ( @binilchengankal )

### \>\> Wait for a minute

### \>\> A reply will be sent as Direct Message

## If any error occured try Installing Locally

# Local Machine Setup Procedure

### \>\> Clone the repository

```
https://github.com/Aaromalchekavar/TuTu_TwitterThreadSaver.git

```
# Setup Virtual Environment (Optional)
### >> To get started, if you’re not using Python 3, you’ll want to install the virtualenv tool with pip:
```
$ pip install virtualenv

```
### >> If you are using Python 3, then you should already have the venv module from the standard library installed.
### >> Change directory to project directy 
```
$ cd <directory_name>

```
### >> Create a new virtual environment inside the directory:
```
# Python 2:
$ virtualenv env

# Python 3
$ python3 -m venv env

```
### >> Activate the Virtual Environment
```
$ source env/bin/activate
(env) $

```
# Setup Twitter Credentials
```
$ export CONSUMER_KEY="<Your Consumer Key>"
$ export CONSUMER_SECRET="<Your Consumer Secret Key>"
$ export ACCESS_TOKEN="<Your Access Tocken>"
$ export ACCESS_TOKEN_SECRET="<Your Access Tocken Secret>"

```
# How to Run
```
$ python main.py

# or

$ python3 main.py

```