from flask import Flask, render_template
from datetime import datetime
import pytz

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def show_time():
    timezone = pytz.timezone("GMT")
    time_now = datetime.now(timezone)
    return render_template('index.html', time=time_now.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

# Define the route for timezone-specific times
@app.route('/timezone/<tz>')
def time_in_timezone(tz):
    try:
        timezone = pytz.timezone(tz)
        time_now = datetime.now(timezone)
        return render_template('timezone.html', timezone=tz, time=time_now.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    except pytz.exceptions.UnknownTimeZoneError:
        return "Invalid timezone", 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
