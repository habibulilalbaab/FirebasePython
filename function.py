import firebase_admin
from firebase_admin import credentials, firestore, storage
import config as cfg

# https://towardsdatascience.com/nosql-on-the-cloud-with-python-55a1383752fc
# https://medium.com/@abdelhedihlel/upload-files-to-firebase-storage-using-python-782213060064

# init connect
cred = credentials.Certificate(cfg.auth_path)
firebase_admin.initialize_app(cred, {'storageBucket': cfg.storageBucket})

db = firestore.client()

def documentList(collection):
    collection = db.collection(collection)
    res = collection.get()
    data = []
    for i in res:
        data.append(i.to_dict())
    return data

def create(collection, document, data):
    collection = db.collection(collection)
    res = collection.document(document).set(data)
    return res

def read(collection, document):
    collection = db.collection(collection)
    doc = collection.document(document)
    res = doc.get().to_dict()
    return res

def query(collection, document, opr, filterVal):
    collection = db.collection(collection)
    doc = collection.where(document, opr, filterVal)
    res = doc.get()
    data = []
    for i in res:
        data.append(i.to_dict())
    return data

def update(collection, document, data):
    collection = db.collection(collection)
    res = collection.document(document).update(data)
    return res

# Untuk tambah data kedalam array dokumen
def arrayUnion(collection, document, array, data):
    collection = db.collection(collection)
    res = collection.document(document).update({
        array: firestore.ArrayUnion(data)
    })
    return res

# Untuk hapus data kedalam array dokumen
def arrayRemove(collection, document, array, data):
    collection = db.collection(collection)
    res = collection.document(document).update({
        array: firestore.ArrayRemove(data)
    })
    return res

def delete(collection, document):
    collection = db.collection(collection)
    res = collection.document(document).delete()
    return res

# untuk hapus salah satu data pada dokumen
def deleteField(collection, document, field):
    collection = db.collection(collection)
    res = collection.document(document).update({field: firestore.DELETE_FIELD})
    return res

def addFile(filename, path):
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(path)
    # Opt : if you want to make public access from the URL
    blob.make_public()
    return blob.public_url

def deleteFile(filename):
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.delete()
    return "success"