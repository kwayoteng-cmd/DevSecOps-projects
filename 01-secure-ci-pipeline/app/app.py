from flask import Flask

app = Flask(Matics_Chrome)

@app.route("/")
def home():
    return "Secure CI Pipeline Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

