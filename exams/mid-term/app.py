from flask import Flask, jsonify, redirect, request
import json
import random


app = Flask(__name__)
DOMAIN = "127.0.0.1:5000/"

#Store all created bitlink data in memory: mapping_data
user_data = []


#Create new user
@app.route('/users', methods=['POST'])
def create_new_user():
    request_data = request.get_json()
    _id = str(random.randint(0, 500))
    _name = request_data['name']
    _email = request_data['email']
    _tweets = []
    _followers = []
    result = dict(id = _id, name = _name, email = _email, tweets = _tweets, followers = _followers)
    user_data.append(result)
    return result

@app.route('/users/<string:user_id>/followers/<string:follower_id>', methods = ['PATCH'])
def create_new_follower(user_id, follower_id):
    print("user_id:", user_id)
    for i in range(len(user_data)):
        print(user_data[i]['id'])
        if user_data[i]["id"] == user_id:
            user_data[i]["followers"].append(follower_id)
            break
            
    
    for user in user_data:
        print(user)
    return user


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
