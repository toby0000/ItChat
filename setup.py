""" A wechat personal account api project
See:
https://github.com/littlecodersh/ItChat
"""
import re
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


__version__ = re.findall(r"VERSION\s*\=\s*'([\w\.\-]+)'",
                         open(path.join(here, 'itchat/config.py')).read())[0]


setup(
    name='itchat',

    version=__version__,

    description='A complete wechat personal account api',
    long_description=long_description,

    url='https://github.com/littlecodersh/ItChat',

    author='LittleCoder',
    author_email='i7meavnktqegm1b@qq.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='wechat itchat api robot weixin personal extend',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    install_requires=['requests', 'pyqrcode', 'pypng', 'blinker'],

    # List additional groups of dependencies here
    extras_require={},
)
