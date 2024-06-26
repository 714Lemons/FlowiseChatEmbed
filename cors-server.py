from flask import Flask, send_from_directory, make_response

app = Flask(__name__)

@app.route('/dist/<path:filename>')
def serve_file(filename):
    try:
        response = make_response(send_from_directory('dist', filename))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    except Exception as e:
        print(f"Error serving file: {e}")
        return '', 500

if __name__ == "__main__":
    app.run(port=8000)
