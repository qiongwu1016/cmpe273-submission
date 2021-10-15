from flask import Flask, jsonify, redirect, request
import json
from markupsafe import escape
import hashlib
from marshmallow import Schema, fields, pprint
from datetime import datetime, date, timedelta
import random


app = Flask(__name__)
DOMAIN = "127.0.0.1:5000/"

#Store all created bitlink data in memory: mapping_data
user_data = []

class UserSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    email = fields.Str()
    sweets = fields.List(fields.Str())
    followers = fields.List(fields.Str())
    


#Create new user
@app.route('/users', methods=['POST'])
def create_new_user():
    request_data = request.get_json()
    schema = UserSchema()
    result = schema.load(request_data)
    _id = random.randint(0, 500)
    _tweets = []
    _followers = []
    result['tweeets'] = _tweets
    result['followers'] = _followers
    result['id'] = _id
    user_data.append(result)
    print(user_data)
    return result

@app.route('/users/<string:user_id>/followers/<string:follower_id>', methods = ['PATCH'])
def create_new_follower(user_id, follower_id):
    print("user_id:", user_id)
    for i in range(len(user_data)):
        print(user_data[i]['id'])
        if user_data[i]["id"] == user_id:
            print("aaaa")
            follower_list = user_data[i]['followers']
            follower_list.append(follower_id)
            print(follower_list)
            
    
    for user in user_data:
        print(user)
    return "follower_" + follower_id + " inserted to user:" + user_id


@app.route('/users/<string:user_id>/tweets', methods = ['POST'])
def post_a_tweet(user_id):
    request_data = request.get_json()
    print(request_data)
    for user in user_data:
        if user['id'] == user_id:
            user['tweets'].append(request_data["tweet"])
            break
    return user

@app.route('/users/<string:user_id>', methods = ['GET'])
def get_user_details(user_id):
    
    for user in user_data:
        if user['id'] == user_id:
            break
    return user

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
