from flask import Blueprint, jsonify

connectionTest_bp = Blueprint('connection_test', __name__)

@connectionTest_bp.route('/connectionTest', methods=['GET'])
def connection_test():
    return jsonify({"message": "Connection Successful"}), 200
