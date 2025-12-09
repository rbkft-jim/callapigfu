from flask import Flask

app = Flask(__name__)

@app.route("/test")
def main():
<<<<<<< HEAD
    return "Hello World de Gfunctions"
=======
    return "Hello World de Gfunction"
>>>>>>> dae9caf (rétablissement du répertoire)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=8080)
