# task 114 - Write a script that tests a provided url is up or not.

import urllib
import urllib.request

url = input("Enter a url: ")

try:
    urllib.request.urlopen(url)
except urllib.error.URLError:
    print("It's not up!")
else:
    print("It's up!")
