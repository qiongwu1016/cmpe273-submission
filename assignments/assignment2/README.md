# Assignment2
Clone Bitlinks APIs

## run app.py

## default domain 

127.0.0.1:5000

## Short a link

### /v4/shorten
methods = post
request body example:
{

"long_url": "https://www.taobao.com/",

"domain": "bit.ly",

"group_guid": "Ba1bc23dE4F"

}

## Create a link
### /v4/bitlinks
methods = post
request body example:
{

"long_url": "https://www.google.com",

"domain": "127.0.0.1:5000/",

"group_guid": "Ba1bc23dE4F",

"title": "Google Home Page",

"tags": [

"google",

"web"

],

"deeplinks": []

}

## Update a link
### /v4/bitlinks/{bitlink}
methods = PATCH
example ..

## Retrieve a link
### /v4/bitlinks/{bitlink}
methods = GET
request example:
127.0.0.1:5000/v4/bitlinks/{127.0.0.1:5000/ac6bb669}


## Get clicks for a bitlink
### /v4/bitlinks/{bitlink}/clicks
methods = GET
request example:
http://127.0.0.1:5000/v4/bitlinks/127.0.0.1:5000/ac6bb669/clicks?unit=day&units=4
