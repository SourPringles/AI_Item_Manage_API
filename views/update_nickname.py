# Base Librarys

# Libraries
from flask import Blueprint, jsonify

# Custom Librarys
from db import load_storage, update_storage


updateNickname_bp = Blueprint('updateNickname', __name__)

@updateNickname_bp.route('/updateNickname/<uid>/<new_name>', methods=['GET'])
def update_nickname(uid, new_name):
    """
    별명 변경 엔드포인트
    """
    # SQL 조회로 최신 인벤토리 반환
    inventory = load_storage()

    for data in inventory:
        if data["uuid"] == uid:
            # uid가 일치하는 경우
            data["nickname"] = new_name
            update_storage(data)
            inventory = load_storage()
            #print(inventory)
            return jsonify({"message": "Nickname updated successfully.", "result": data})

    return "ok", 500