from flask import Blueprint, request, jsonify

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return jsonify(search_users(request.args.to_dict())), 200


def sort_users(user):
    args = request.args.to_dict()
    if 'id' in args and user['id'] == args['id']:
        return 0
    elif 'name' in args and args['name'].lower() in user['name'].lower():
        return 1
    elif 'age' in args and (int(args['age']) - 1 <= user['age'] <= int(args['age']) + 1):
        return 2
    elif 'occupation' in args and args['occupation'].lower() in user['occupation'].lower():
        return 3
    else:
        return 4
    
    
    
def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    filtered_users = []
    
    
    #id param
    if 'id' in args:
        user = next((user for user in USERS if user['id'] == args['id']), None)
        if user:
            filtered_users.append(user)
    
   
    #name param    
    if 'name' in args:
        name_query = args['name'].lower()
        for user in USERS:
            if name_query in user['name'].lower():
                if user not in filtered_users:
                    filtered_users.append(user)       
    
    
    #age param
    if 'age' in args:
        age_query = int(args['age'])
        for user in USERS:
            if age_query - 1 <= user['age'] <= age_query + 1:
                if user not in filtered_users:
                    filtered_users.append(user)
        
    #Occupation param
    if 'occupation' in args:
        occupation_query = args['occupation'].lower()
        for user in USERS:
            if occupation_query in user['occupation'].lower():
                if user not in filtered_users:
                    filtered_users.append(user)
     
    
    filtered_users.sort(key=sort_users)
             
    return filtered_users
