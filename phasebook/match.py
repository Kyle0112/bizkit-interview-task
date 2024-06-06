import time
from flask import Blueprint, jsonify

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if not 0 <= match_id < len(MATCHES):
        return jsonify({"error": "Invalid match id"}), 404
    
    start = time.time()
    
    try:
        match_found = is_match(*MATCHES[match_id])
        msg = "Match found" if match_found else "No Match"
    
    except Exception as e:
        return jsonify({"error": str(e)}), 200    
    end = time.time()

    return jsonify({"message": msg, "elapsedTime": end - start}), 200


def is_match(fave_numbers_1, fave_numbers_2):
    if not isinstance(fave_numbers_1, list) or not isinstance(fave_numbers_2, list):
        raise ValueError("Inputs must be lists")
    
    fave_numbers_set = set(fave_numbers_1)
    for number in fave_numbers_2:
        if number not in fave_numbers_set:
            return False
            
    return True
