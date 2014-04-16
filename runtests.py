# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import os

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

TEMPLATE_DIRS = (
    rel('example/example/templates'),
)

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'simple_sso.sso_server',
    'simple_sso',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'simple_sso.test_urls'

def run_tests():
    from django.conf import settings
    settings.configure(
        INSTALLED_APPS=INSTALLED_APPS,
        ROOT_URLCONF=ROOT_URLCONF,
        DATABASES=DATABASES,
        TEMPLATE_DIRS=TEMPLATE_DIRS,
        TEST_RUNNER='django.test.simple.DjangoTestSuiteRunner',
        SSO_PRIVATE_KEY='private',
        SSO_PUBLIC_KEY='public',
        SSO_SERVER='http://localhost/server/',
    )
    # Monkey patch the Client urls for testing
    from simple_sso.sso_client.client import Client

    def get_request_token(self, redirect_to):
        return self.consumer.consume('/server/request-token/', {'redirect_to': redirect_to})['request_token']
    Client.get_request_token = get_request_token

    def get_user(self, access_token):
        user_data = self.consumer.consume('/server/verify/', {'access_token': access_token})
        user = self.build_user(user_data)
        return user
    Client.get_user = get_user

    # Run the test suite, including the extra validation tests.
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)

    test_runner = TestRunner(verbosity=1, interactive=False, failfast=False)
    failures = test_runner.run_tests(['simple_sso'])
    return failures


if __name__ == "__main__":
    failures = run_tests()
    if failures:
        sys.exit(bool(failures))
