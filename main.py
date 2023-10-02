import urllib.request

url = 'https://github.com/ViggoRogestam/grupparbete-programering1'
filename = 'my_module.py'
urllib.request.urlretrieve(url, filename)

from my_module import my_function
