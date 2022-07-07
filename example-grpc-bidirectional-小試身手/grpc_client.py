import os, sys, logging, time, json, argparse, grpc
from google.protobuf import empty_pb2, json_format
import datetime
import example_pb2 
import example_pb2_grpc

def run(host, port, api_key, auth_token, timeout, use_tls):
    """Makes a basic call against a gRPC server."""
    # ==================> Create channel <==================
    if use_tls:
        creds = grpc.ssl_channel_credentials()
        channel = grpc.secure_channel('{}:{}'.format(host, port), creds)
    else:
        print(host, port)
        channel = grpc.insecure_channel('{}:{}'.format(host, port))
    try:
        stub = example_pb2_grpc.BidirectionalStreamExampleStub(channel) 
    except Exception as e:
        print(e)
    metadata = []
    if api_key:
        metadata.append(('x-api-key', api_key))
    if auth_token:
        metadata.append(('authorization', 'Bearer ' + auth_token))
    
    # ==================> Custom Test Script <==================
    print("--------------Call BidirectionalStreamingMethod Begin---------------")
    test_list = ['j', 'i', 'm', 'm', 'y', ' ', 'i', 's', ' ', 'h', 'a', 'n', 'd', 's', 'o', 'm', 'e', ' ', 'EOF']
    # create a generator
    def request_messages(test_list):
        for i in range(len(test_list)):
            time.sleep(1)
            request = example_pb2.CharRequest(
                character=test_list[i])
            yield request

    response_iterator = stub.CharStream(request_messages(test_list))
    for response in response_iterator:
        print("response string: ", response.words)

    print("--------------Call BidirectionalStreamingMethod Over---------------")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--host', default='localhost', help='The host to connect to')
    parser.add_argument(
        '--port', type=int, default=8080, help='The port to connect to')
    parser.add_argument(
        '--timeout', type=int, default=360, help='The call timeout, in seconds')
    parser.add_argument(
        '--api_key', default=None, help='The API key to use for the call')
    parser.add_argument(
        '--auth_token', default=None,
        help='The JWT auth token to use for the call')
    parser.add_argument(
        '--use_tls', type=bool, default=False,
        help='Enable when the server requires TLS')
    args = parser.parse_args()
    run(args.host, args.port, args.api_key, args.auth_token, args.timeout, args.use_tls)