from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Reimagining Shopping Backend is Running!"

@app.route("/api/test")
def test():
    return jsonify({
        "message": "Backend connected successfully",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)