from requests import get, post

# Send "get" http requests:
res = get("http://www.google.com")

# Check, page is loaded or not:
if res.status_code == 404 or is not 200:
  print("You have an error to load page!")
else:
  print("GET requests sent successfuly!")

# You can access response test
code = res.text
print(code)

# Post requests:
URL = "Your site address"
data = [{
  key: value
}]
req_post = post(URL, data)

# As you can check again loading
