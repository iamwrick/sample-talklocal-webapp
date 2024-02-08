
from flask import Flask, send_from_directory, render_template
from flask_socketio import SocketIO


app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('subtitle_viewer.html')

# Define a route to serve the .vtt file
@app.route('/subtitle/<path:filename>')
def serve_subtitle(filename):
    # Assuming your .vtt files are stored in a 'subtitles' directory
    return send_from_directory('subtitle', filename)

if __name__ == '__main__':
    app.run(port=5001, debug=True)

