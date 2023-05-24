from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def home():
    if(request.method == 'POST'):
        data = request.get_json()
        print(data)
    return "hi"


app.run(port=5000)
