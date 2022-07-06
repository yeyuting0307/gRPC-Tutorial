# template-grpc
## 撰寫流程 

---
### 1. 確認背景設定

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
    action.proto
```
---
### 4. 撰寫 `server.py` & `client.py`

本地端測試API需要先在背景啟動server，在另執行client(預設port=8080)

```
python3 grpc_server.py
python3 grpc_client.py
```

---



