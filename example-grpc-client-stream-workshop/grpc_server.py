import os, logging, argparse, time, json, grpc
from concurrent import futures
import example_pb2 
import example_pb2_grpc

class apiServer(example_pb2_grpc.ClientStreamExample):
    ''' Implement grpc API server '''
    def __init__(self, *args, **kwargs): 
        return None

    def ExampleRpc(self, requests, context, *args, **kwargs):
        ''' What does this api do ? '''
        ''' client stream type '''
        print("ClientStreamingMethod called by client...")

        total_times = 0

        for request in requests:
            print("recv from client(%d)" %
                  (request.client_stream_render_times))
            total_times += request.client_stream_render_times

        return example_pb2.ExampleResponse(
            res_content=f"Python server clientStreaming Ok!!!! Sum of client id is {total_times}"
        )

def serve(port, shutdown_grace_duration):
    """Configures and runs the API server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ClientStreamExampleServicer_to_server(
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