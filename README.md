# RestApiUdemy
 Proof of work

# Routes

### /login
> '@app.route("/login_without_cookies", methods=["POST"])
def login_without_cookies():
    access_token = create_access_token(identity="example_user")
    return jsonify(access_token=access_token)'

### /items
### /item


## Guide partially followed
https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/33781648#overview

## Documentation followed
https://flask-jwt-extended.readthedocs.io/en/stable/

https://flask.palletsprojects.com/en/2.3.x/

https://github.com/corydolphin/python-bcrypt/blob/master/README.md