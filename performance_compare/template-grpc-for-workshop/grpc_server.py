#%%
import os, logging, argparse, time, json, grpc
from concurrent import futures
import action_pb2 as api_handler_pb2 # FIXME: GENERATED_pb2
import action_pb2_grpc as api_handler_pb2_grpc # FIXME: GENERATED_pb2_grpc
from threading import Thread
import datetime
from google.protobuf.any_pb2 import Any
from grpc_reflection.v1alpha import reflection
# from dotenv import load_dotenv
# load_dotenv('.env')


#%%
# ========================== Server ==========================
# FIXME: MyService
class apiServer(api_handler_pb2_grpc.ToDoServiceServicer):
    ''' Implement grpc API server '''
    def __init__(self, *args, **kwargs): 
        self.service_id = 1

    def HealthCheck(self, request, context, *args, **kwargs):
        print('check')
        return api_handler_pb2.HealthCheckRes(
            status_code = 200,
            status_msg = 'success',
        )

    def UnaryAddItem(self, request, context, *args, **kwargs):
        ''' unary type '''
        print('name: ', request.name)
        print('price: ', request.price)
        print('message: ', request.message)

        listObj = api_handler_pb2.List()
        for idx in range(5):
            ItemObj = api_handler_pb2.Item()
            ItemObj.price = idx
            ItemObj.name = 'name' + str(idx)
            ItemObj.message = 'message' + str(idx)

            listObj.items.extend([ItemObj])
        # print('listObj >> ', listObj)

        return listObj

def serve(port, shutdown_grace_duration):
    """Configures and runs the bookstore API server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # FIXME: MyService
    api_handler_pb2_grpc.add_ToDoServiceServicer_to_server(
        apiServer(), server)

    SERVICE_NAMES = (
        api_handler_pb2.DESCRIPTOR.services_by_name['ToDoService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    print('Listening on port {}'.format(port))

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(shutdown_grace_duration)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--port', type=int, default=None,
        help='The port to listen on.'
             'If arg is not set, will listen on the $PORT env var.'
             'If env var is empty, defaults to 8080.')
    parser.add_argument(
        '--shutdown_grace_duration', type=int, default=5,
        help='The shutdown grace duration, in seconds')
    args = parser.parse_args()
    port = args.port
    if not port:
        port = os.environ.get('PORT')
    if not port:
        port = 8080
    serve(port, args.shutdown_grace_duration)
