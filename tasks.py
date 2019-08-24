from invoke import task


@task
def dist(c):
    c.run('python setup.py sdist')


@task
def uploadtest(c):
    c.run('python -m twine upload ' +
          '--repository-url https://test.pypi.org/legacy/ dist/*')


@task
def upload(c):
    c.run('python -m twine upload dist/*')
