from flask import Flask

app = Flask(__name__)

@app.route("/test")
def main():
    return "Hello World de Gfunctions v2"

#Add a comment
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=8080)
