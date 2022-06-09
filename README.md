### Installation
* Make python virtual environment
    ```
    python3 -m venv <venv_location>
    cd <venv_location>
    ```
* Clone this repository inside venv
    ```
    git init
    git remote add origin https://github.com/habibulilalbaab/FirebasePython.git
    git fetch
    git branch master origin/main
    git checkout master
    ```
* Install Dependency
    ```
    pip install firebase-admin
    pip install flask
    ```
* Configuration file config.py
    ```
    auth_path = "auth/foo.json" # masukkan lokasi json autentikasi
    storageBucket = "foo.appspot.com" # masukkan bucket name firebase storage
    ```
    Untuk mengubah port url api, bisa edi di api.py pang bawah, ubah port 5000 dengan yang diinginkan
* Running service
    masuk ke folder virtual env yang telah dibuat & jalankan
    ```
    bin/python3 api.py &
    ```
### Endpoint
```
[GET] /api/literature
```
Respone example:
```
[
  {
    "classification": "foo",
    "description": "foo",
    "image": "foo",
    "literature_id": "",
    "name": "foo",
    "origin": "foo"
  },
  {
    "classification": "foo",
    "description": "foo",
    "image": "foo",
    "literature_id": "",
    "name": "foo",
    "origin": "foo"
  }
]
```