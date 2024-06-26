from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Serve files from the dist directory
@app.route('/dist/<path:filename>')
def dist_files(filename):
    dist_dir = os.path.join(app.root_path, 'dist')
    return send_from_directory(dist_dir, filename)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
