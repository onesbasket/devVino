from devVino.form import KakikomiForm

def test(request):
    f = KakikomiForm(request.GET)
    f.is_valid()
    print "^^^^^^^^^^^^^^^^^"
    print f['lowPrice'].get('lowPrice')
    print "000000000000000"
    return f