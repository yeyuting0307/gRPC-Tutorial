# template-grpc-python

## Summary 
---
這隻GRPC API在做什麼？

MyService(gRPC):
- myRpc1: 我會做....
- myRpc2: 我在做....

---
### API Info

Service URL: `{CLOUD_RUN_API_URL}`

Test gRPC: 

```
python3 grpc_client.py \
    --host {CLOUD_RUN_API_URL} \
    --port 443 \
    --use_tls true       
```


---
---

## 撰寫流程 

---
### 1. 確認背景設定

- 先確認gcloud背景設定，並切換到正確的`project`
    ```
    gcloud config list
    ```
- 確認本地端有googleapis(僅執行一次，後續請自行pull最新版本)
    > 解析成REST API需要 `google/api/annotations.proto`
    ```
    cd {where-to-clone-googleapis-folder}
    git clone https://github.com/googleapis/googleapis
    ```
---
### 2. 撰寫`.proto`檔案

---
### 3. 生成`pb.py`與`pb_grpc.py`

```

python3 -m grpc_tools.protoc \
    --proto_path=. \
    --python_out=. \
    --grpc_python_out=. \
    example.proto
```

### 4. 撰寫 `server.py` & `client.py`

本地端測試API需要先在背景啟動server，在另執行client(預設port=8080)

```
python3 grpc_server.py
python3 grpc_client.py
```

---
---


