import grpc
from concurrent import futures
import time
import pymongo
import json

# import the generated classes
import replicator_pb2
import replicator_pb2_grpc
from grpc_reflection.v1alpha import reflection

#Connect to Mongodb: database "college" - collection "students" 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["college"]
mycol = mydb["students"]

def insert(data):
  item = {
    "id":data['columnvalues'][0],
    "first_name" :data['columnvalues'][1], 
    "last_name": data['columnvalues'][2], 
    "sjsu_id": data['columnvalues'][3], 
    "email":data['columnvalues'][4], 
    "create_timestamp":data['columnvalues'][5], 
    "update_timestamp":data['columnvalues'][6]
    }
  mycol.insert_one(item)
  print('Data inserted...', 'id:',data['columnvalues'][0] )
  pass

def update(data):
  myquery = { "id": data['columnvalues'][0]}
  item = {
    "$set": {
      "id":data['columnvalues'][0],
      "first_name" :data['columnvalues'][1], 
      "last_name": data['columnvalues'][2], 
      "sjsu_id": data['columnvalues'][3], 
      "email":data['columnvalues'][4], 
      "create_timestamp":data['columnvalues'][5], 
      "update_timestamp":data['columnvalues'][6]
    }
  }
  mycol.update_many(myquery, item)
  print('Data updated...','id:', data['columnvalues'][0])
  print()
  pass

def delete(data):
  myquery = { "id": data['oldkeys']['keyvalues'][0]}
  mycol.delete_many(myquery)
  print('Data deleted...', 'id:', data['oldkeys']['keyvalues'][0])
  pass

def replicate(x):
    obj = json.loads(x)
    # print(json.dumps(obj))  
    
    for i in obj['change']:
        if i['kind']=='insert':
           insert(i)
        if i['kind']=='update':
            update(i)
        if i['kind']=='delete':
            delete(i)
    
    return x

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class LogicCopyServicer(replicator_pb2_grpc.LogicCopyServicer):

    def logicCopy(self, request, context):
        response = replicator_pb2.Wal()
        response.value = replicate(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
replicator_pb2_grpc.add_LogicCopyServicer_to_server(
        LogicCopyServicer(), server)

# enable reflection
service_names = [
  reflection.SERVICE_NAME,
  'LogicCopy',
]
reflection.enable_server_reflection(service_names, server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)