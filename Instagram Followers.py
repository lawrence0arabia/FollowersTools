# INSTAGRAM FOLLOWER SCRIPT -- Ryan Lawrence https://github.com/lawrence0arabia

# Checks a chosen Instagram account's followers and following and generates .txt
# files for both, then compares the files and generates a third "scum" file of
# accounts who don't follow back.

# Python 3.8.0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time, os

options = Options()
options.headless = True

print("[Firefox must be installed and configured to use with Selenium]\n[Temporary restrictions may be placed on your account for unfollowing too quickly]\n[All locally processed, check the source code to confirm. Don't run if you don't understand]\n")

user_username = input("What's your Instagram username?\n")
password = input("What's your Instagram password?\n")
username = input("What account do you want to check?\n")
directory = input("Where would you like to save the .txt files generated by this script?\n[Full path required]")

browser = webdriver.Firefox(options=options)

# LOGGING INTO INSTAGRAM ----------------------------------------------------------

browser.get('https://instagram.com')
time.sleep(1)
# Finding log username field and password field
usernameField = browser.find_element_by_name("username")
passwordField = browser.find_element_by_name("password")
time.sleep(1)
# Sending username and password
usernameField.send_keys(user_username)
passwordField.send_keys(password)
# Find and click login button
logInButton = browser.find_element_by_css_selector('.L3NKy > div:nth-child(1)')
logInButton.click()
time.sleep(2.7)

# Going to page and checking followers and following
browser.get('https://www.instagram.com/' + username)
# Print some stats
followers = browser.find_element_by_css_selector('li.Y8-fY:nth-child(2) > a:nth-child(1) > span:nth-child(1)')
print('\nFollowers: ' + followers.text)
following = browser.find_element_by_css_selector('li.Y8-fY:nth-child(3) > a:nth-child(1) > span:nth-child(1)')
print('\nFollowing: ' + following.text)
difference = int(followers.text) - int(following.text)
print('\nDifference: ' + str(difference))
percentage = (int(followers.text) / int(following.text))*100
followingNumber = following.text
print()
print(str(round(percentage, 2)) + '% of people follow ' + username + ' back')

# FOLLOWERS LIST ----------------------------------------------------------------------------------------------

# Open followers box by clicking followers button, wait for load
followers.click()
time.sleep(0.5)

# Find follower box to scroll in 
followersBox = browser.find_element_by_css_selector('.isgrP')

# Scroll down to load all followers
for i in range(int(followers.text)-1):
    followersBox.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.10)

# Generate 'follower' list, list of all followers, traversable with follower[x], do follower[x].text to get their username
follower = browser.find_elements_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg.HYpXt div._1XyCr div.isgrP ul.jSC57._6xe7A div.PZuss li.wo9IH div.uu6c_ div.t2ksc div.enpQJ div.d7ByH span.Jv7Aj.mArmR.MqpiF a.FPmhX.notranslate._0imsa')

# Open and clear plaintext file containing followers for that username
followersListText = open(directory + username + '_followers.txt', 'w')

# Write followers to text file
print('\nWriting followers to text file...')
for i in range(int(followers.text)-1):
    followersListText.write(str(follower[i].text) + '\n')
followersListText.close()

# FOLLOWING LIST ----------------------------------------------------------------------------------------------

# Reload the page (to close following box)
browser.get('https://www.instagram.com/' + username)
time.sleep(0.5)

# Find following button again because we reloaded
following = browser.find_element_by_css_selector('li.Y8-fY:nth-child(3) > a:nth-child(1) > span:nth-child(1)')

# Open following box by clicking following button, wait for load
following.click()
time.sleep(0.5)

# Find following box to scroll in
followingBox = browser.find_element_by_css_selector('.isgrP')

#Scroll down to load all following
for i in range(int(followingNumber)-1):
    followingBox.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.10)

# Generate 'following' list, list of all people you're following, traversable with following[x], do following[x].text to get their username
following = browser.find_elements_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg.HYpXt div._1XyCr div.isgrP ul.jSC57._6xe7A div.PZuss li.wo9IH div.uu6c_ div.t2ksc div.enpQJ div.d7ByH span.Jv7Aj.mArmR.MqpiF a.FPmhX.notranslate._0imsa')

# Open and clear plaintext file containing following for that username
followingListText = open(directory + username + '_following.txt', 'w')

# Write following to text file
print('Writing following to text file...')
for i in range(int(followingNumber)-1):
    followingListText.write(str(following[i].text) + '\n')
followingListText.close()

# NOT FOLLOWING BACK LIST -------------------------------------------------------------------------------------

print('Writing scum to text file...')

f1 = open(directory + username + '_followers.txt', "r") 
f2 = open(directory + username + '_following.txt', "r")

# Create dictionaries by reading the lines of f1 and f2
dict1 = f1.readlines()
dict2 = f2.readlines()

# Create a few more dictionaries, to compare the lines, keeping only lines from f2 which don't appear in f1
diff1 = [ x for x in dict2 if x not in dict1 ]
diff2 = [ x for x in dict1 if x not in dict2 ]
diff3 = [ x for x in diff1 if x not in diff2 ]

# Create a 3rd file
f3 = open(directory + username + '_scum.txt', "w")

# Write lines from f2 which don't appear in f1
for x in range(len(diff3)):
	f3.write(str(diff3[x].strip()) + '\n')
f3.close()
browser.quit()
