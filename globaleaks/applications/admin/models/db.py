# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

if MULTI_USER_MODE:
    db = DAL('sqlite://storage.sqlite')       # if not, use SQLite or other DB
    from gluon.tools import *
    mail = Mail()                                  # mailer
    auth = Auth(globals(),db)                      # authentication/authorization
    crud = Crud(globals(),db)                      # for CRUD helpers using auth
    service = Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc
    plugins = PluginManager()

    settings.mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
    settings.mail.settings.sender = 'you@gmail.com'         # your email
    settings.mail.settings.login = 'username:password'      # your credentials or None

    settings.auth.hmac_key = '<your secret key>'   # before define_tables()
    settings.auth.define_tables()                           # creates all needed tables
    settings.auth.mailer = mail                    # for user email verification
    settings.auth.registration_requires_verification = False
    settings.auth.registration_requires_approval = True
    settings.auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['verify_email'])+'/%(key)s to verify your email'
    settings.auth.reset_password_requires_verification = True
    auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['reset_password'])+'/%(key)s to reset your password'

    db.define_table('app',Field('name'),Field('owner',db.auth_user))

if not session.authorized and MULTI_USER_MODE:
    if auth.user and not request.function=='user':
        session.authorized = True
    elif not request.function=='user':
        redirect(URL('default','user/login'))

def is_manager():
    if not MULTI_USER_MODE:
        return True
    elif auth.user and auth.user.id==1:
        return True
    else:
        return False
