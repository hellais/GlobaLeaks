response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%s <%s>' % (settings.author, settings.author_email)
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
    (T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
    (T('Submission'),URL('submission', 'index')==URL(),URL('submission','index'),[]),
    (T('Receiver'), '/receiver'==URL(), '/receiver', []),
    (T('Node View'), '/globalview'==URL(), '/globalview', []),
    (T('Targets'),'/targets'==URL(), '/targets'),
    (T('Groups'),'/groups'==URL(),'/groups'),
    # (T('Tulips'),URL('tulip','index')==URL(),URL('tulip','index'),[]),
    # "Tulips" redirect to index, why keeping that ? 
]

