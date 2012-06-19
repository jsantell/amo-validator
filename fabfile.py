"""
Basic fabfile to setup environment for running tests
"""
import functools
import os

from fabric.api import local, run

ROOT = os.path.abspath(os.path.dirname(__file__))

os.environ['PYTHONPATH'] = os.pathsep.join([ROOT,
                                            os.path.join(ROOT, 'validator')])

local = functools.partial(local, capture=False)

def test(pdb=False):
    cmd = 'nosetests'

    if pdb:
        cmd += ' --pdb --pdb-failures -s'

    local(cmd)


def install():
    # Setup virtualenv if it's not already set up.
    if not run('which workon'):
        run('easy_install virtualenv')
        run('wget http://bitbucket.org/dhellmann/virtualenvwrapper/raw/'
            'f31869779141/virtualenvwrapper_bashrc -O ~/.virtualenvwrapper')
        run('mkdir ~/.virtualenvs')
        run('export WORKON_HOME=~/.virtualenvs')
        run('source ~/.virtualenvwrapper')

    run('pip install -r requirements.txt')
    run('git submodule update --init')

