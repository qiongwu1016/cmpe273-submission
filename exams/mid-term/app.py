from flask import Flask, jsonify, redirect, request
import json
import random


app = Flask(__name__)
DOMAIN = "127.0.0.1:5000/"

#Store all created bitlink data in memory: mapping_data
user_data = []
global_weet_id =1
global_id = 100


#Create new user
@app.route('/users', methods=['POST'])
def create_new_user():
    global global_id
    request_data = request.get_json()
    _id = str(global_id)
    global_id = global_id + 1
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
            
    return user_data[i]


@app.route('/users/<string:user_id>/tweets', methods = ['POST'])
def post_a_tweet(user_id):
    global global_weet_id
    request_data = request.get_json()
    print(request_data)
    for user in user_data:
        if user['id'] == user_id:
            _tweet_content = request_data["tweet"]
            _tweet_id = str(global_weet_id)
            global_weet_id = global_weet_id + 1
            _tweet = {"tweet_id": _tweet_id, "tweet": _tweet_content}

            user['tweets'].append(_tweet)
            break
    return user

@app.route('/users/<string:user_id>', methods = ['GET'])
def get_user_details(user_id):
    
    for user in user_data:
        if user['id'] == user_id:
            break
    return user



@app.route('/users/<string:user_id>/timeline', methods = ['GET'])
def get_tweets_from_user(user_id):
    user_list = []
    for user in user_data:
        if user['id'] == user_id:
            user_list.append(user_id)
            for follower in user["followers"]:
                user_list.append(follower)

    tweet_id_list =[]
    records = []
    for user in user_data:
        if user["id"] in user_list:
            for tweet in user["tweets"]:
                if tweet["tweet_id"] not in tweet_id_list:
                    records.append(dict(user_id = user["id"], tweet_id = tweet["tweet_id"], tweet = tweet["tweet"]))
                    tweet_id_list.append(tweet["tweet_id"])
    result = dict(timeline =  records)
    return result


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
