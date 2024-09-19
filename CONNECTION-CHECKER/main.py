import urllib.request as urlib



def connectionUrl(url):

    print("checking")

    response= urlib.urlopen(url)

    print(f"Connection to: {url} was succesful")

    print(f"The response was: {response.getcode()}")

print("WELCOME TO THIS PROGRAM , IT HELP YOU TO IDENTIFY A CONNECTION ABOUT A SITE")

url_input = input("Enter the url \n")


connectionUrl(url_input)