from django import template


register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.filter(name='lookup')
def lookup(value, arg, default=""):
    if arg in value:
        return value[arg]
    else:
        return default


from jinja2.ext import Extension

#class url_replace(Extension):
#    tags = set(['url_replace'])
#
#    def parse(self, parser):
#        lineno = parser.stream.next().lineno
#        args = [parser.parse_expression()]
#        print parser.parse_expression()
#        dict_ = request.GET.copy()
#        dict_[field] = value
#        return dict_.urlencode()
