from flask import Flask

app = Flask(helloFrame)

@app.route("/")
def Hello():
    return "Hello World, Woo-oo!"
    
