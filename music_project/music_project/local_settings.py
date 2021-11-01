SECRET_KEY = 'django-insecure-%&r9-%pj05by2vhu98)vx__j(wqj7vbe@53-)14260%6&0ov%a'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library',
        'USER': 'root',
        'PASSWORD': 'Programming!@34',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}