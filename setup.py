try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1.1'

with open('requirements/production.txt') as requirements_file:
    requires = [item for item in requirements_file]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()  # pylint: disable=redefined-builtin

setup(
    name='powerlibs-aws-lambda-deployer',
    version=version,
    description="Set of tools to deploy and configure AWS Lambda functions",
    long_description=readme,
    author='Adolfo W. Sabino',
    author_email='adolfo.w.s@gmail.com',
    url='https://github.com/Dronemapp/powerlibs-aws-lambda-deployer',
    license=license,
    packages=['powerlibs.aws.λ.deployer'],
    package_data={'': ['README.md']},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='generic libraries',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
