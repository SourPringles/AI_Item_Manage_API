# Base Librarys

# Libraries
from flask import Blueprint, jsonify

# Custom Modules


connectionTest_bp = Blueprint('connection_test', __name__)

@connectionTest_bp.route('/connectionTest', methods=['GET'])
def connection_test():
    """
    연결테스트
    """
    return "Connection Successful", 200
