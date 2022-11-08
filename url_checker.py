print("1.Domain Information Report")
print("2.Checking for Malicious url(URL Report) ")
opt=int(input("Select the Option to Check: "))

domain=str(input("Enter the Domain name: "))

api = open("api.txt","r+") 
  
import requests

url = 'https://www.virustotal.com/vtapi/v2/domain/report'

params = {'apikey':api,'domain':domain}

response1 = requests.get(url, params=params)


api = open("api.txt","r+")  

url = 'https://www.virustotal.com/vtapi/v2/url/report'

params = {'apikey':api, 'resource':domain}

response2 = requests.get(url, params=params)


if opt==1:
    print(response1.json())
elif opt==2:
    print(response2.json())
else:
    print("Enter valid input")
