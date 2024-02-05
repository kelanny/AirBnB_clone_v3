#!/usr/bin/python3
"""Created a flask view route
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """Gets the app status"""
    return jsonify({"status": "OK"})
