# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""Zabbix helper scripts.
"""

from setuptools import setup, find_packages
import glob
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='zeit.zabbix',
    version='1.0.0.dev0',

    install_requires=[
        'pyzabbix',
        'setuptools',
    ],

    extras_require={
        'test': [
            'mock',
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [
            'zabbixmaintenance = zeit.zabbix.maintenance:main',
        ],
    },

    author='Wolfgang Schnerring <wolfgang.schnerring@zeit.de>',
    author_email='wolfgang.schnerring@zeit.de',
    license='ZPL 2.1',
    url='https://github.com/zeitonline/zeit.zabbix/',

    keywords='',
    classifiers="""\
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 2 :: Only
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.rst',
        'CHANGES.txt',
    )),

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('', glob.glob(project_path('*.txt')))],
    zip_safe=False,
)
