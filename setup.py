from setuptools import setup

requires = [
    "flask",
    "flask_classful",
    "rethinkdb",
    "jsonschema",
    "pyfunctional"
]

setup(
    name='flask-rethinkview',
    version='0.2',
    packages=["flask_rethinkview"],
    url='https://github.com/lucidfrontier45/flask-rethinkview',
    license='MIT',
    author='Shiqiao Du',
    author_email='lucidfrontier.45@gmail.com',
    description='RESTful Flask View with RethinkDB',
    install_requires=requires
)
