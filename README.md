# gRPC-Tutorial

## [gRPC教學文件](https://fluff-motorcycle-78c.notion.site/0a4394f8028046418d61d38cdfb3b2eb?v=45efbe4b6df54f3fa7eceded311d267c)


---
## gRPC撰寫流程 

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



