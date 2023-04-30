from flask import Blueprint, jsonify
from models  import db, User, Planet, Character, Vehicule, Post, Favourites #la clase

api = Blueprint("api", __name__)

@api.route('/users', methods=['GET'])
def handle_get_users():
    users = db.session.query(User).all()
    # users = User.query.all()
    
    users = list(map(lambda user : user.serialize(), users))
 
    return jsonify(users), 200

@api.route('/users/favourites', methods=['GET'])
def handle_get_user_favourites():

    my_users = db.session.query(User).all()

    user_favourites = [user.my_fav_list() for user in my_users if user.is_active]
    print(user_favourites)

    return jsonify(user_favourites), 200

@api.route('/people', methods=['GET'])
def handle_get_characters():
    people = db.session.query(Character).all()
    
    people = list(map(lambda peopleitem : peopleitem.serialize(), people))
 
    return jsonify(people), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def handle_get_single_character(people_id):
    my_character = Character.query.get(people_id)

    return jsonify(my_character.serialize()), 200

@api.route('/planets', methods=['GET'])
def handle_get_planets():
    planets = db.session.query(Planet).all()
    
    planets = list(map(lambda planetitem : planetitem.serialize(), planets))
 
    return jsonify(planets), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def handle_get_sinlge_planet(planet_id):

    my_planet = Planet.query.get(planet_id)

    return jsonify(my_planet.serialize()), 200

# @api.route('/vehicules', methods=['GET'])
# def handle_get_vehicules():
#     vehicules = db.session.query(Vehicule).all()
    
#     vehicules = list(map(lambda vehiculeitem : vehiculeitem.serialize(), vehicules))
 
#     return jsonify(vehicules), 200

# @api.route('/vehicules/<int:vehicule_id>', methods=['GET'])
# def handle_get_sinlge_vehicule(id):

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def handle_add_planet_as_favourite_to_user(planet_id):

    my_active_user = User.query.filter_by(is_active=True).first()
    my_searched_planet = Planet.query.filter_by(id=planet_id).first()

    new_favourite = Favourites(
        user_id = my_active_user.id,
        post_id =my_searched_planet.post[0].id
    )
    db.session.add(new_favourite)
    db.session.commit()


    return f"Planet added to favourites of {my_active_user.username}", 200

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def handle_add_character_as_favourite_to_user(people_id):

    my_active_user = User.query.filter_by(is_active=True).first()
    my_searched_character = Character.query.filter_by(id=people_id).first()

    new_favourite = Favourites(
        user_id = my_active_user.id,
        post_id =my_searched_character.post[0].id
    )
    db.session.add(new_favourite)
    db.session.commit()


    return f"Character added to favourites of {my_active_user.username}", 200

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def handle_delete_favourited_planet_from_user(planet_id):

    my_active_user = User.query.filter_by(is_active=True).first()
    
    #encontrar el fav a eliminar
    post_for_item = Post.query.filter_by(planet_media_id=planet_id).first() #se supone un post por elemento
    target_favourite_to_delete = Favourites.query.filter_by(user_id = my_active_user.id).filter_by(post_id=post_for_item.id).first()

    #borrar el objeto de la tabla fav
    db.session.delete(target_favourite_to_delete)
    db.session.commit()

    return f"Planet deleted from favourites of {my_active_user.username}", 200

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def handle_delete_favourited_character_from_user(people_id):

    my_active_user = User.query.filter_by(is_active=True).first()

    #encontrar el fav a eliminar
    post_for_item = Post.query.filter_by(character_media_id=people_id).first() #se supone un post por elemento
    target_favourite_to_delete = Favourites.query.filter_by(user_id = my_active_user.id).filter_by(post_id=post_for_item.id).first()

    #borrar el objeto de la tabla fav
    db.session.delete(target_favourite_to_delete)
    db.session.commit()

    return f"Character deleted from favourites of {my_active_user.username}", 200