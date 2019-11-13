
import os.path
import urllib.request, urllib.error, urllib.parse
import glob
from fabric.api import run, cd, local, lcd, prefix, get, put

# FIXME directories below depend on version!


# --------------- documentation

def deploy_doc():
    with cd('/home/ug/www.u-go.net/uligo04-bb'):
        run('hg pull -u')  # note: as a prerequisite, the repository must be in the right branch!
    with cd('/home/ug/www.u-go.net/uligo04-bb/doc'):
        run('rm -rf ../../dl/uligo/doc')
        run('sphinx-build -A ugonet_online=1 -b html . ../../dl/uligo/doc')


def doc_as_pdf():
    with prefix('source /home/ug/.virtualenvs/uligo04-bb/bin/activate'):
        with lcd('/home/ug/devel/uligo04-bb/doc'):
            local('make clean')
            local('make latex')
            local('cp sphinx.sty _build/latex/')
    with lcd('/home/ug/devel/uligo04-bb/doc/_build/latex/'):
        local('make all-pdf')
        local('mv uligo.pdf uligo-0.4.pdf')


# --------------- pootle

LANGUAGES = [os.path.basename(lang) for lang in  glob.glob('lang/*') if os.path.basename(lang).find('.') == -1]
LANGUAGES.remove('en')


def pootle_start_maintenance():
    run('sudo a2dissite pootlek')
    run('sudo a2ensite pootlek-maintenance')
    run('sudo service apache2 reload')


def pootle_end_maintenance():
    run('sudo a2dissite pootlek-maintenance')
    run('sudo a2ensite pootlek')
    run('sudo service apache2 reload')


def download_po(ignore_errors=False):
    with prefix('source /home/ugy/.virtualenvs/pootlekombilo/bin/activate'):
        with cd('/home/ugy/devel/pootlekombilo/Pootle-2.1.6'):
            run('./manage.py sync_stores --project uligo')

    with lcd('lang'):
        for lang in LANGUAGES:
            with lcd('%s/LC_MESSAGES' % lang):
                try:
                    get('/home/ugy/devel/pootlekombilo/Pootle-2.1.6/po/uligo/%s/uligo.po' % lang, './uligo.po')
                except:
                    if not ignore_errors:
                        raise
                else:
                    local('msgfmt -o uligo.mo uligo.po')


def upload_pot_new():
    upload_pot(ignore_errors=True)


def upload_pot(ignore_errors=False):
    '''Adds new strings to po files/removes unecessary ones. To do this:

    * obtain the current po files from pootle
    * create new pot file using pygettext
    * apply msgmerge
    * upload the merged files to pootle
    '''

    pootle_start_maintenance()
    download_po(ignore_errors=ignore_errors)

    # create new pot file:
    with prefix('source /home/ug/.virtualenvs/uligo04-bb/bin/activate'):
        with lcd('src'):
            local('pygettext -p ../lang/ uligo.py')

    with lcd('lang'):
        # update uligo.po file for "en"
        local('msgmerge -U en/LC_MESSAGES/uligo.po messages.pot')

        # merge other po files and upload them to pootle
        for lang in LANGUAGES:
            local('msgmerge -U %s/LC_MESSAGES/uligo.po messages.pot' % lang)
            with lcd('%s/LC_MESSAGES' % lang):
                local('msgfmt -o uligo.mo uligo.po')
                put('uligo.po', '/home/ugy/devel/pootlekombilo/Pootle-2.1.6/po/uligo/%s/uligo.po' % lang, mode=0o660)
                run('chgrp www-data /home/ugy/devel/pootlekombilo/Pootle-2.1.6/po/uligo/%s/uligo.po' % lang)

    with prefix('source /home/ugy/.virtualenvs/pootlekombilo/bin/activate'):
        with cd('/home/ugy/devel/pootlekombilo/Pootle-2.1.6'):
            run('./manage.py update_stores --project uligo')

    pootle_end_maintenance()


# --------------- uligo main/linux

def deploy_targz():
    with lcd('/home/ug/devel'):
        local('mkdir uligo')
        local('rm -f uligo-0.4.tar.gz')
        local('hg clone uligo04-bb uligo')
    with lcd('/home/ug/devel/uligo/'):
        local('hg update default')

    with prefix('source /home/ug/.virtualenvs/uligo04-bb/bin/activate'):
        with lcd('/home/ug/devel/uligo/doc'):
            local('make html')
    with lcd('/home/ug/devel/uligo'):
        local('rm */*.pyc')
        local('rm */*/*.pyc')
        local('rm -rf .hg')
        local('rm -f fabfile.py')
    with lcd('/home/ug/devel'):
        local('tar cfz uligo-0.4.tar.gz uligo')
        local('rm -rf uligo')


# --------------- uligo main/windows installer


def win_py2exe():
    with lcd(r'c:\Users\ug\uligo\src'):
        # clean up
        if os.path.exists('dist'):
            local('rd /q /s dist')
        local('python setup.py py2exe')


def win_innosetup():
    # copy stuff for innosetup
    # vcredist_x86.exe: http://www.microsoft.com/download/en/confirmation.aspx?id=5582

    for f in ['uligo.ico']:
        local('copy /y c:\\Users\\ug\\uligo\\%s \\Users\\ug\\uligo\\src\\dist\\ ' % f)

    # build docs
    with lcd(r'c:\Users\ug\uligo\doc'):
        local('sphinx-build -b html . ..\src\dist\doc')

    # add source archive
    u = urllib.request.urlopen('https://bitbucket.org/ugoertz/uligo/get/default.zip')
    with open('c:\\Users\\ug\\uligo\src\dist\\uligo-source.zip', 'wb') as f:
        f.write(u.read())

    # innosetup
    with lcd(r'c:\Users\ug\uligo'):
        local(r'"c:\Program Files\Inno Setup 5\ISCC" uligo.iss')


def deploy_win():
    win_py2exe()
    win_innosetup()
