# ___________________________ requests module ___________________________
import requests

# ______ Read and Fetch data ______
# First get a request and then fetch a response from a server.
"""r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

#1
print("Status:",r.status_code)
#2
print("URL:",r.url)
#3
print("\nHeaders:",r.headers,"\n")
#4
print("\nRaw text:",r.text[:120],"\n") # first 120 characters

#5
if "application/json" in ("Content-Type",""):   #check if server sent JSON format
    data = r.json()     #convert JSON into python dictionary
    print("As Dictionary:",data) 
else:       #otherwise raw text format
    print(r.text)

"""

# ______ Parameters in the URL ______
"""
# without params
r = requests.get("https://jsonplaceholder.typicode.com/posts")
print("URL:", r.url)
print("Items:",len(r.json()))

# with params
params = {"userId": 2}
r = requests.get("https://jsonplaceholder.typicode.com/posts", params = params)
print("\nURL:", r.url)
print("Items:",len(r.json()))

# we can also use list of tuples as params
# params = [("color", "black"), ("size", 42)]
"""

# ______ Status Codes ______
"""
r = requests.get("https://github.com/shehaankhurram")
print("Status:",r.status_code) # it will print 200

# 2xx success(200 OK, 201 created)
# 3xx redirects
# 4xx client errors(404 not found, 401 unauthorized)
# 5xx server issue(500, 503)"""


# ______ Sending Data ______
"""
data = {"Name": "Shehaan", "Age": 20, "userId": 2}
#send json body(Most mordern APIs)
r = requests.post("https://jsonplaceholder.typicode.com/posts", json = data) #application/json set successfully.

print("Status Code:",r.status_code)
print("Data:",r.json())
"""

#send HTML body(old styles)
form = {"Username":"Shehaan", "password":"Shehaan123"}
r = requests.post("https://jsonplaceholder.typicode.com/posts", data = form)
print("Status Code:",r.status_code)
print("Data:",r.json())





