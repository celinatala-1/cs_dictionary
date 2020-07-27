from flask import Flask, url_for

app = Flask(__name__)
@app.route('/')
def main_screen():
    return "Welcome to my CS Dictionary"

@app.route('/goodbye')
def goodbye():
    return "Goodbye, World"

with app.test_request_context():
    print(url_for('main_screen'))

if __name__ == '__main__':
    app.run()
