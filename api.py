# api.py
from flask import Flask, jsonify
from scraper import traverse_and_get_links

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger_traverse():
    try:
        traverse_and_get_links()
        return jsonify({"status": "success", "message": "traverse_and_get_links triggered successfully."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
