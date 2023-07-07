# RestApiUdemy
 Proof of work

# Routes

### /login
#### Request, json:
##### body:
```json
{
  "username": "plainText",
  "password": "plainText"
}
```
#### Response, json
##### body:
```json
{
  "access-token": "<token>",
  "refresh-token": "<token>"
}
```

### /items - jwt required
#### Request, json
##### headers:
```json
{
    "Authorization": "Bearer <token>"
}
```
##### body:
```json
{
    "store": "plainText"
}
```
### /item - jwt required


## Guide partially followed
https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/33781648#overview

## Documentation followed
https://flask-jwt-extended.readthedocs.io/en/stable/

https://flask.palletsprojects.com/en/2.3.x/

https://github.com/corydolphin/python-bcrypt/blob/master/README.md