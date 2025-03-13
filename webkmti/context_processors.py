def is_voter(request) : 
    return {'is_voter' : request.user.groups.filter(name='voter').exists()}
def is_admin(request) : 
    return {'is_admin' : request.user.groups.filter(name='admin').exists()}