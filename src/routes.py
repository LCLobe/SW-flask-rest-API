from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route('/users', methods=['GET'])
def handle_get_users():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/users/favourites', methods=['GET'])
def handle_get_user_favourites():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/people', methods=['GET'])
def handle_get_characters():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def handle_get_single_character():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/planets', methods=['GET'])
def handle_get_planets():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def handle_get_sinlge_planet():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def handle_add_planet_as_favourite_to_user():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def handle_add_character_as_favourite_to_user():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def handle_delete_favourited_planet_from_user():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def handle_delete_favourited_character_from_user():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200