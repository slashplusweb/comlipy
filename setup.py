import re
from os import path

from setuptools import find_packages, setup

_ABSOLUTE_DOC_LINK = re.compile(r'\[(?P<text>[^\]]+)\]\((?P<link>\/{0,1}docs\/[^\)]*)\)')


def _absolute_docs_link_replacement(text):
    def _replacement(m):
        return '[{text}](https://gitlab.com/slashplus-build/comlipy/blob/master/{link})'.format(
            text=m.group('text'),
            link=m.group('link')
        )

    return _ABSOLUTE_DOC_LINK.sub(_replacement, text)


# read the contents of the README file
package_path = path.abspath(path.dirname(__file__))
with open(path.join(package_path, 'README.md'), encoding='utf-8') as f:
    long_description = _absolute_docs_link_replacement(f.read())

setup(
    name='comlipy',
    description='comlipy by slashplus - lint commit messages with python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.1.2',
    author='slashplus',
    author_email='info@slashplus.de',
    url='https://gitlab.com/slashplus-build/comlipy/',
    install_requires=[
        'Click',
        'pyyaml',
    ],
    license='MIT',
    py_modules=['comlipy'],
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['config-comlipy.yml']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        comlipy=comlipy.main:cli
    """,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Systems Administration',
    ],
)
