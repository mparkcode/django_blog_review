def is_an_author(request):
    is_an_author = request.user.groups.filter(name = 'authors').exists()
    return{"is_an_author" : is_an_author}
