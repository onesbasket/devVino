def user_name(request):
    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    return {"uname": request.GET.get('lowPrice'),
             "aaaa":"abc",}
