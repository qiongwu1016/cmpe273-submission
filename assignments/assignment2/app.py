from flask import Flask, jsonify, redirect
import json
from flask import request
from markupsafe import escape
import hashlib
import model
from datetime import datetime, date, timedelta

app = Flask(__name__)
DOMAIN = "127.0.0.1:5000/"

#Store all created bitlink data in memory: mapping_data
mapping_data = []

#Hash long string to short string
def cheaphash(string,length=8):
    if length<len(hashlib.sha256(string.encode('utf-8')).hexdigest()):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()[:length]
    else:
        raise Exception("Length too long. Length of {y} when hash length is {x}.".format(x=str(len(hashlib.sha256(string).hexdigest())),y=length))

#Redirect short link to long url, default domain is local host. 
@app.route('/<string:hash>')
def hello(hash):
    bitlink = DOMAIN + hash
    long_url = DOMAIN
    for dict in mapping_data:
        if dict['id'] == bitlink:
            long_url = dict['long_url']
            if dict.get('clicks_list') == None:
                clicks_list = []
                clicks_list.append(datetime.now())
                dict['clicks_list'] = clicks_list
            else:
                clicks_list = dict['clicks_list']
                clicks_list.append(datetime.now())
                dict['clicks_list'] = clicks_list
            break
    return redirect(long_url, code=302)

#Short a long url. Create a bitlink stored in memory. Return the bitlink info in json format
@app.route('/v4/shorten', methods=['POST'])
def shorten_a_link():
    request_data = request.get_json()

    #read long_url from request body
    long_url = request_data['long_url']
    domain = request_data['domain']
    group_guid = request_data['group_guid']
    short_url = cheaphash(long_url)
    id = DOMAIN + short_url
    link = "http://"+ id
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S+0000")
    result_dict = dict(link = link, long_url = long_url, created_at = date_time, id = id)
    mapping_data.append(result_dict)
    schema = model.BitLinkSchema()
    result = schema.dump(result_dict)
    # return json.dumps(result, sort_keys=True, indent=4)
    return result

#Create a bitlink with additional infomation. Return the bitlink info in json format
@app.route('/v4/bitlinks', methods = ['POST'])
def create_a_link():
    request_data = request.get_json()
    long_url = request_data['long_url']
    group_guid = request_data['group_guid']
    title = request_data['title']
    tags = request_data['tags']

    deeplink_list = []
    for link  in request_data['deeplinks']:
        app_id = link['app_id']
        app_uri_path = link['app_uri_path']
        install_url = link['install_url']
        install_type = link['install_type']
        deeplink_dict = dict(app_id = app_id, app_uri_path = app_uri_path, install_url = install_url, install_type = install_type, guid = group_guid)
        deeplink_schema = model.DeepLinkSchema()
        deeplink = deeplink_schema.dump(deeplink_dict)
        deeplink_list.append(deeplink)

    short_url = cheaphash(long_url)
    id = DOMAIN + short_url
    link = "http://"+ id
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S+0000")
    result_dict = dict(link = link, long_url = long_url, created_at = date_time, id = id, title = title,  tags = tags, deeplinks = deeplink_list)
    mapping_data.append(result_dict)
    return json.dumps(result_dict, sort_keys = True, indent = 4)

#Update a bitlink, return the bitlink info in json format
@app.route('/v4/bitlinks/<string:domain>/<string:hash>', methods = ['PATCH'])
def update_a_link(domain, hash):
    request_data = request.get_json()
    id = domain + "/" + hash
    for i in range(len(mapping_data)):
        if mapping_data[i]['id'] == id:
            del mapping_data[i]
            break
    mapping_data.append(request_data)

    return request_data

#Retrieve a bitlink
@app.route('/v4/bitlinks/<string:domain>/<string:hash>', methods = ['GET'])
def retrieve_a_link(domain, hash):
    id = domain + "/" + hash
    for i in range(len(mapping_data)):
        if mapping_data[i]['id'] == id:
            break
    return mapping_data[i]
            

#Returns the click counts for the specified link in an array based on a date
@app.route('/v4/bitlinks/<string:domain>/<string:hash>/clicks', methods = ['GET'])
def get_clicks(domain, hash):
    id = domain + "/" + hash
    unit = request.args.get("unit")
    if unit == None:
        unit = 'day'
    units = request.args.get("units")
    if units == None:
        units = -1
    
    record = None
    for data in mapping_data:
        if data['id'] == id:
            record = data
            break


    if units == -1:
        _units = 100
    else:
        _units = int(units)
    today = datetime.now().date()
    list = []
    for i in range(_units):
        delta = timedelta(days = i)
        date = today - delta
        clicks = 0
        for r in record['clicks_list']:
            if r.date() == date:
                clicks = clicks + 1
        if clicks != 0:
            clicks_dict = dict(clicks = clicks, date = r.strftime("%Y/%m/%d"))
            list.append(clicks_dict)
        
    clicks_dict = dict(clicks = list, units = units, unit = unit)

    return clicks_dict


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)


