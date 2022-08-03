from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_World():
    return "Hello"
if __name__=="__main__":
    app.run(debug=True)