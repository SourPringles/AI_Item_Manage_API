from flask import Blueprint, request, jsonify
from db import load_storage, update_storage

rename_bp = Blueprint('rename', __name__)

@rename_bp.route('/rename/<qr_code>/<new_name>', methods=['POST'])
def rename(qr_code, new_name):
    """
    별명 변경 엔드포인트
    """
    # SQL 조회로 최신 인벤토리 반환
    inventory = load_storage()

    # QR 코드로 항목 찾기
    if qr_code in inventory:
        inventory[qr_code]["nickname"] = new_name
        update_storage(qr_code, inventory[qr_code])
        inventory = load_storage()
        return jsonify({"message": "Nickname updated successfully.", "inventory": inventory})
    else:
        return jsonify({"error": f"Item with QR code '{qr_code}' not found."}), 404