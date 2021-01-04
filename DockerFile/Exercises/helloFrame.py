from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello Duckberg, Woo-oo!"

if __name__ == "__main__":
    app.run(debug=True)
