DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    #    'NAME': 'cyp',                        # Or path to database file if using sqlite3.
    #    'USER': 'root',                       # Not used with sqlite3.
    #    'PASSWORD': 'password',               # Not used with sqlite3.
    #    'HOST': '127.0.0.1',                  # Set to empty string for localhost. Not used with sqlite3.
    #    'PORT': '3306',                       # Set to empty string for default. Not used with sqlite3.
    #}
    
    #Free MYSQL Hosting @
    #http://www.freemysqlhosting.net/account/
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sql217303',                        # Or path to database file if using sqlite3.
        'USER': 'sql217303',                       # Not used with sqlite3.
        'PASSWORD': 'sF6*iF8%',               # Not used with sqlite3.
        'HOST': 'sql2.freemysqlhosting.net',                  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                       # Set to empty string for default. Not used with sqlite3.
    }
}