from flask import Flask, request, render_template, jsonify, send_from_directory, render_template_string
from datetime import datetime
import pytz
from pytz import timezone

app = Flask(__name__, static_url_path='')


@app.route('/')
def home():
    return render_template('index.html', timezones=pytz.all_timezones)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/get-time')
def get_time():
    format = "%Y-%m-%d %H:%M:%S"
    return jsonify({
        'time': datetime.now().strftime(format)
    })


@app.route('/time-converter')
def time_converter():
    tz = request.args.get('tz', 'UTC')
    format = '%Y-%m-%d %H:%M:%S %Z%z'

    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))

    # Convert to User requested time zone
    now_tz = now_utc.astimezone(timezone(tz))

    return jsonify({
        'time': now_tz.strftime(format)
    })


if __name__ == '__main__':
    app.run(debug=True)


