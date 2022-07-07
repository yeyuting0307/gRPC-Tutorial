import os, logging, argparse, time, json, grpc, datetime
from concurrent import futures
import example_pb2 
import example_pb2_grpc
from threading import Thread

class apiServer(example_pb2_grpc.BidirectionalStreamExample):
    ''' Implement grpc API server '''
    def __init__(self, *args, **kwargs): 
        return None

    def BidirectionalStream(self, requests, context, *args, **kwargs):
        ''' bidirectional stream type '''
        
        print("BidirectionalStreamingMethod called by client...")

        # Open a sub thread to receive data
        def parse_request():
            for request in requests:
                print("now: ", datetime.datetime.now())
                print("server recv from client(%d), message= %s" %
                      (request.client_id, request.request_data))
                

        thread_work = Thread(target=parse_request)
        thread_work.start()

        for i in range(6):
            time.sleep(2)
            yield example_pb2.ExampleResponse(
                server_id = i ,
                response_data=("send by Python server, message= %d" % i))
                

        thread_work.join()
        print('Done')

def serve(port, shutdown_grace_duration):
    """Configures and runs the API server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_BidirectionalStreamExampleServicer_to_server(
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