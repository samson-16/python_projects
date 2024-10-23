import pyshorteners

url = input ("Enter the url: ")

shortener = pyshorteners.Shortener()

print("The short url is: ",shortener.tinyurl.short(url))

