# FollowersTools
Python scripts to manage your Instagram account. Generate a list of everyone who doesn't follow you back, and feed that list into another script to automatically unfollow them.

[Firefox must be installed and configured to use with Selenium]
[Temporary restrictions may be placed on your account for unfollowing too quickly]
[All locally processed, check the source code to confirm. Don't run if you don't understand]

# Instagram Followers.py 
Checks a chosen Instagram account's followers and following and generates .txt files for both. 
Then compares the files and generates a third "scum.txt" file of accounts who don't follow back.

# Unfollower
Iterates through a .txt file of Instagram accounts and unfollows them. 
Has speed options to avoid Instagram limiting your account.
~40 unfollows per hour seems to be the sweet spot.
