# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from djangocms_hubspot import __version__

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Framework :: Django',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

REQUIREMENTS = [
    'django>=1.8',
    'django-cms>=3.4',
    'django-select2',
]

setup(
    name="djangocms-hubspot",
    version=__version__,
    url='https://github.com/Blueshoe/djangocms-hubspot',
    license='MIT',
    description="Django-CMS Plugin which integrates HubSpot",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Maximilian Muth',
    author_email='max@blueshoe.de',
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    keywords=['django', 'Django CMS', 'hubspot', 'forms'],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False,
)
