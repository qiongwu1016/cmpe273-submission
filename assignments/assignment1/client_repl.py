# from grpc_requests import client
# import time

# client = client.Client.get_by_endpoint("localhost:50051")
# client.request('LogicCopy', 'logicCopy', {"value": "test"})



# import grpc
import time
import json
from grpc_requests import client

#Open and keep reading the WAL.file
f = open('WAL.file','r')
buffer = ""

client = client.Client.get_by_endpoint("localhost:50051")
print('Waiting for WAL.file being updated...')
while 1 :
    line = f.readline()
    if not line:
        time.sleep(2.4)
    else:
        buffer = buffer + line
        if line == "}\n" : 
            print('--------------------------')
            print('Sending a WAL update request message...')

            # make the call
            response = client.request('LogicCopy', 'logicCopy', {"value": buffer})
            obj = json.loads(response['value'])
            print(json.dumps(obj,  indent=3))
            print("This Wal updated...")

            buffer = ""

















