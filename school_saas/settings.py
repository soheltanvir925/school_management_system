from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ba=$l$lzdrhhstp)c_iv=(%7b)dgu8&@iv_vhe(074vma@myld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['localhost', '.localhost', '127.0.0.1']
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'academy.localhost', 'dreamacademy.localhost']

# Application definition
SHARED_APPS = [
    'django_tenants',  # mandatory
    'customers', 
    'django.contrib.staticfiles',
    'django.contrib.sessions',  
    'django.contrib.messages', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'home_auth',
    # ... other global apps
]

TENANT_APPS = [
    'django.contrib.auth', 
    'django.contrib.sessions',  
    'django.contrib.messages', 
    'students',            
    'exams',
    'finance',
    'school',
    'home_auth',
]

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]



TENANT_MODEL = "customers.Client" # Your School model
TENANT_DOMAIN_MODEL = "customers.Domain"

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'school_saas.tenant_urls'
PUBLIC_SCHEMA_URLCONF = 'school_saas.urls'
TENANT_URLCONF = 'school_saas.tenant_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'school_saas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'school_saas_db',
        'USER': 'saas_admin',
        'PASSWORD': 'Dream925@$',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
# এখানে BASE_DIR এর সাথে আপনার ফোল্ডারের নাম যোগ করুন
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

AUTH_USER_MODEL = 'home_auth.CustomUser'
