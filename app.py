from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Emilie trollar hit och dit! Detta uppdaterades automatiskt! Snyggt va?'

if __name__ == '__main__':
    import os
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() in ('1', 'true', 'yes')
    app.run(host=host, port=port, debug=debug)