# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_pb2 as example__pb2


class ClientStreamExampleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExampleRpc = channel.stream_unary(
                '/my.server.streaming.grpc.ClientStreamExample/ExampleRpc',
                request_serializer=example__pb2.ExampleRequest.SerializeToString,
                response_deserializer=example__pb2.ExampleResponse.FromString,
                )


class ClientStreamExampleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExampleRpc(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientStreamExampleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExampleRpc': grpc.stream_unary_rpc_method_handler(
                    servicer.ExampleRpc,
                    request_deserializer=example__pb2.ExampleRequest.FromString,
                    response_serializer=example__pb2.ExampleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'my.server.streaming.grpc.ClientStreamExample', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientStreamExample(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ExampleRpc(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/my.server.streaming.grpc.ClientStreamExample/ExampleRpc',
            example__pb2.ExampleRequest.SerializeToString,
            example__pb2.ExampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
