import function as fs

# ============================================================ Create Example
data = {
    'lat': 41.3851,
    'long': 2.1734,
    'weather': 'great',
    'landmarks': [
        'guadí park',
        'gaudí church',
        'gaudí everything'
    ]
}
fs.create('document','lipsum', data)

# ============================================================ Read Example
fs.read('document','ytjzFfIESnMnZt5UhJq7')

# ============================================================ Update Example bisa juga untuk tambah data yang sudah ada
data = {
    'landmarks': [
        'Borobudur',
        'Prambanan'
    ]
}
fs.update('document','lipsum', data)

# ============================================================ Update atau tambah data kedalam array dokumen
data = ['Tikus']
fs.arrayUnion('document','lipsum', 'landmarks', data)

# ============================================================ Remove data yang ada didalam array dokumen
data = ['Tikus', 'Borobudur']
fs.arrayRemove('document','lipsum', 'landmarks', data)

# ============================================================ Delete salah satu data di dokumen
fs.deleteField('document','lipsum', 'weather')

# ============================================================ Query
fs.query('document', 'lat','>', 0)

# ============================================================ Delete dokumen
fs.delete('document','lipsum')

# ============================================================ Add file storage
fs.addFile('requirements.txt', 'requirements.txt')

# ============================================================ Delete file storage
fs.deleteFile('requirements.txt')