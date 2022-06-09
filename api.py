from flask import Flask, jsonify
import function as fs

# GET
# name = request.args.get('name')
# POST
# record = json.loads(request.data)
app = Flask(__name__)
defaultMsg = {'status': 'success','message': 'Please refrence to endpoint !'}
@app.route('/')
def index():
    return jsonify(defaultMsg)
@app.route('/api')
def api():
    return jsonify(defaultMsg)

@app.route('/api/literature', methods=['GET'])
def literature():
    return jsonify(fs.documentList('literature'))

app.run(host="localhost", port=5000, debug=True)