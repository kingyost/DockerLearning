from app import app

@app.route('/')
def duck():
	return "Hello Ducktales, Woo-oo!"
