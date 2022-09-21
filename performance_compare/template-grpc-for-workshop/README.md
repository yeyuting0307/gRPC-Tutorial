docker build -t asia-east1-docker.pkg.dev/aiii-developer/develop/template-grpc-for-workshop-jimmy . --platform linux/amd64; 

docker push asia-east1-docker.pkg.dev/aiii-developer/develop/template-grpc-for-workshop-jimmy

gcloud run deploy \
--image asia-east1-docker.pkg.dev/aiii-developer/develop/template-grpc-for-workshop-jimmy \
--platform managed \
--allow-unauthenticated \
--memory="512Mi"


python -m grpc_tools.protoc \ 
    --proto_path=${GOOGLEAPIS_DIR} \
    --proto_path=. \
    --python_out=. \
    --descriptor_set_out=./api_descriptor.pb \
    --grpc_python_out=. \
    action.proto


python3 -m grpc_tools.protoc \
    --proto_path=. \
    --descriptor_set_out=./api_descriptor.pb \
    --python_out=. \
    --grpc_python_out=. \
    action.proto