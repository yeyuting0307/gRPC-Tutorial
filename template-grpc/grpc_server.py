#%%
import os, logging, argparse, time, json, grpc
from concurrent import futures
import GENERATED_pb2 as api_handler_pb2 # FIXME: GENERATED_pb2
import GENERATED_pb2_grpc as api_handler_pb2_grpc # FIXME: GENERATED_pb2_grpc
# from dotenv import load_dotenv
# load_dotenv('.env')


#%%
# ========================== Server ==========================
# FIXME: MyService
class apiServer(api_handler_pb2_grpc.MyServiceServicer):
    ''' Implement grpc API server '''
    def __init__(self, *args, **kwargs): 
        pass
    # FIXME: myRpc1
    def myRpc1(self, request, context, *args, **kwargs):
        ''' What does this api do ? '''
        from util.basic import jsonEncoder
        response_code = 200
        status_msg = ""
        data_object = {} 

        ## TODO: deal with param1
        param1 = request.myParam1

        return api_handler_pb2.myRpc1Response(
            status_code = response_code,
            status_msg = status_msg,
            data_layer =  json.dumps(data_object, cls = jsonEncoder)
        )
    # FIXME: myRpc2
    def myRpc2(self, request, context, *args, **kwargs):
        ''' What does this api do ? '''
        from util.basic import jsonEncoder
        response_code = 200
        status_msg = ""
        data_object = {} 

        return api_handler_pb2.myRpc2Response(
            status_code = response_code,
            status_msg = status_msg,
            data_layer = json.dumps(data_object, cls = jsonEncoder)
        )

def serve(port, shutdown_grace_duration):
    """Configures and runs the bookstore API server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # FIXME: MyService
    api_handler_pb2_grpc.add_MyServiceServicer_to_server(
        apiServer(), server)

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
