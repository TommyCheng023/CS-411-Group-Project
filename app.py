from flask import Flask, render_template, jsonify
from config import Config
from yotpo_client import YotpoClient

# Initialization
app = Flask(__name__)
yotpo_client = YotpoClient()
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reviews/<product_id>')
def get_product_reviews(product_id):
    try:
        reviews = yotpo_client.get_reviews(product_id)
        return jsonify(reviews)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run()

"""
STUFF TO ADD FOR LOGIN BACKEND:
1. Login
2. Callback
3. Logout
"""