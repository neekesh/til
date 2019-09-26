from flask import Flask
import json
app = Flask(__name__)
hash_data =  {'date':'epoch format', 'data':'I learned about web development topics (frontend, backend, db)'},{'date':'epoch format', 'data':'I found the falsk module'}

@app.route('/veiw')
def json_data():
  return json.dumps(hash_data)
