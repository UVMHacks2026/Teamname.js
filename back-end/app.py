from flask import Blueprint, request, jsonify
from services.plaid_service import exchange_public_token

plaid_bp = Blueprint("plaid", __name__)

@plaid_bp.route("/plaid/exchange", methods=["POST"])
def exchange():
    data = request.json
    public_token = data["public_token"]

    access_token = exchange_public_token(public_token)

    return jsonify({"message": "Token exchanged"})