from flask import Flask, jsonify, request
from scraper import traverse_and_get_links, download_by_url
import threading

app = Flask(__name__)
traverse_lock = threading.Lock()

# Asynchronous trigger endpoint
@app.route('/trigger', methods=['POST'])
def trigger_traverse():
    # Run traverse in a separate thread
    thread = threading.Thread(target=trigger_traverse_async)
    thread.start()
    return jsonify({"status": "success", "message": "Traverse triggered asynchronously."})

def trigger_traverse_async():
    with traverse_lock:
        traverse_and_get_links()

@app.route('/downloadUrl', methods=['POST'])
def download_url():
    data = request.json
    href = data.get("href")
    try:
        download_by_url(href)
        return jsonify({"status": "success", "message": "Download triggered successfully."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5051)
