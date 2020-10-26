# INSTAGRAM UNFOLLOWER -- Ryan Lawrence https://github.com/lawrence0arabia

# Automatically unfollows a specified .txt list of accounts.

# Python 3.8.0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time, os

options = Options()
options.headless = True 

# USER INPUT ----------------------------------------------------------------------

print("[Firefox must be installed and configured to use with Selenium]\n[Temporary restrictions may be placed on your account for unfollowing too quickly]\n[Locally processed, check the source code to confirm. Don't run if you don't understand]\n")
username = input("What's your Instagram username?\n")
password = input("What's your Instagram password?\n")

f1 = open(input('What file do you want to use as input? \n[Input entire directory. Must be a .txt file with 1 username per line and no additional formatting]\n'))
dict1 = f1.readlines()
sleepTime = 1200 / int(input("How many accounts do you want to unfollow per hour? \nInstagram may restrict features of your account if you unfollow too quickly. \n[Recommended ~40 per hour.]\n"))
sleepTime = round(sleepTime)

browser = webdriver.Firefox(options=options)

# LOGGING INTO INSTAGRAM ----------------------------------------------------------

browser.get('https://instagram.com')
time.sleep(1)
# Finding log username field and password field
usernameField = browser.find_element_by_name('username')
passwordField = browser.find_element_by_name('password')
time.sleep(1)
# Sending username and password
usernameField.send_keys(username)
passwordField.send_keys(password)
# Find and click login button
logInButton = browser.find_element_by_css_selector('.L3NKy > div:nth-child(1)')
logInButton.click()
time.sleep(2.7)
following = 0

# STATS FUNCTION ------------------------------------------------------------------
def stats(): # Gets the stats for the account and prints them
    browser.get('https://instagram.com/' + username)
    followers = browser.find_element_by_css_selector('li.Y8-fY:nth-child(2) > a:nth-child(1) > span:nth-child(1)')
    print('\nFollowers: ' + followers.text)
    following = browser.find_element_by_css_selector('li.Y8-fY:nth-child(3) > a:nth-child(1) > span:nth-child(1)')
    print('\nFollowing: ' + following.text)
    difference = int(followers.text) - int(following.text)
    print('\nDifference: ' + str(difference))
    percentage = (int(followers.text) / int(following.text))*100
    print()
    print(str(round(percentage, 2)) + '% of people follow ' + username + ' back\n')

# UNFOLLOW FUNCTION ---------------------------------------------------------------

def unfollow(account):
    try: # There are actually two different types of unfollow buttons, which Instagram uses at random, so this try and except statement catches both
        unfollowButton = browser.find_element_by_css_selector('._6VtSN')
    except:
        unfollowButton = browser.find_element_by_css_selector('button.sqdOP:nth-child(1)')
    if unfollowButton.text != 'Follow': # Since the follow and unfollow button have the same identifiers, we check to make sure we're not about to click follow accidentally
        unfollowButton.click()
        time.sleep(sleepTime)
        unfollowConfirm = browser.find_element_by_css_selector('button.aOOlW:nth-child(1)')
        unfollowConfirm.click()
        print('Unfollowed ' + str(account))

# BEFORE UNFOLLOWING STATS --------------------------------------------------------
print('Your stats before unfollowing...')
stats()

# UNFOLLOWING --------------------------------------------------------------------- 
for x in range(len(dict1)):
    browser.get('https://instagram.com/' + str(dict1[x].strip()))
    time.sleep(sleepTime)
    unfollow(dict1[x].strip())
    time.sleep(sleepTime)

# FINISH --------------------------------------------------------------------------
print('\nFinished unfollowing! \nYour new stats are...')
stats()
browser.quit()
