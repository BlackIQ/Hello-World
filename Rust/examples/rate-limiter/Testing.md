#POSTMAN TESTING
1.
- request url: `localhost:8080`
- request mode: `GET`
- request body: ``
- response:
```json
{
    "headers": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "host": "localhost:8080",
        "postman-token": "58d1840c-901f-48ea-b7da-cc81c204ca04",
        "user-agent": "PostmanRuntime/7.39.1"
    },
    "stored_body": "",
    "stored_method": "GET",
    "stored_path": "/"
}
```

2.
- request url: `localhost:8080/hello`
- request mode: `POST`
- request body: `hello guyz`
- response:
```json
{
    "headers": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "content-length": "10",
        "content-type": "text/plain",
        "host": "localhost:8080",
        "postman-token": "718421ee-f7c8-40c3-98e1-b6684739087e",
        "user-agent": "PostmanRuntime/7.39.1"
    },
    "stored_body": "hello guyz",
    "stored_method": "POST",
    "stored_path": "/hello"
}
```
