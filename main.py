from database_mdb import my_db
from url_shortener import Url
from flask import Flask, request, redirect, jsonify
app = Flask(__name__)


@app.route('/get')
def get_short_url():
    try:
        real_url = request.args.get('url')
        if request.args.get('lifetime') is not None:
            lifetime = int(request.args.get('lifetime'))
        else:
            lifetime = 90
        url = Url(real_url, lifetime)
        my_db.add_new_url(url)
        short = url.create_short_url()
        return jsonify({'url': short})
    except Exception as e:
        return jsonify({"Error:": "Please enter correct parameters [url, lifetime] in format: "
                                  "http://127.0.0.1:5000/get?url=<your url>&lifetime=<yourlifetime>"})


@app.route('/g/<hash_id>')
def resolve(hash_id):
    try:
        real_url = my_db.find_original_url(hash_id)
        return redirect(real_url['original_link'], code=302)
    except Exception as e:
        return jsonify({"Error": "Check your short url for correctness"})


if __name__ == '__main__':
    app.run()

