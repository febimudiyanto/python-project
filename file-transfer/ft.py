import urllib.request

url = input("url = ")
filename = input("file name = ")

urllib.request.urlretrieve(url,filename)