from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def imlearning():
    return "Testing"
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')