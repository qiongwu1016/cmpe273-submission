# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import replicator_pb2 as replicator__pb2


class LogicCopyStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.logicCopy = channel.unary_unary(
        '/LogicCopy/logicCopy',
        request_serializer=replicator__pb2.Wal.SerializeToString,
        response_deserializer=replicator__pb2.Wal.FromString,
        )


class LogicCopyServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def logicCopy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LogicCopyServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'logicCopy': grpc.unary_unary_rpc_method_handler(
          servicer.logicCopy,
          request_deserializer=replicator__pb2.Wal.FromString,
          response_serializer=replicator__pb2.Wal.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'LogicCopy', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
