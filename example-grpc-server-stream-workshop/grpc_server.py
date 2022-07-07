import os, logging, argparse, time, json, grpc
from concurrent import futures
import example_pb2 
import example_pb2_grpc

class apiServer(example_pb2_grpc.ServerStreamExample):
    ''' Implement grpc API server '''
    def __init__(self, *args, **kwargs): 
        return None

    def ExampleRpc(self, request, context, *args, **kwargs):
        ''' What does this api do ? '''
        server_render_times = request.server_render_times
        print(server_render_times)
        for i in range(server_render_times):
            yield example_pb2.ExampleResponse(
                res_content = f"{i+1}_render"
            )

def serve(port, shutdown_grace_duration):
    """Configures and runs the bookstore API server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ServerStreamExampleServicer_to_server(
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