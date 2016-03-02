def user_name(request):
     return {"uname": request.GET.get('lowPrice')}
