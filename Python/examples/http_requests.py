from requests import get, post

# Send "get" http requests:
req = get("http://www.google.com")

# Check, page load or not:
if req.status_code == 404 or is not 200:
  print("You have an error to load page!")
else:
  print("Get requests sent successfuly!")

# You can have code page:
code = req.text
print(code)

# Post requests:
URL = "You site address"
data = [{
  key: value
}]
req_post = post(URL, data)

# As you can check again loading
