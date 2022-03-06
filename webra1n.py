from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        print("hi")

    return render_template('index.html')



app.run()


