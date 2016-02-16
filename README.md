# cli-quickstart

Quickstart template for new python command line tools

Features:

* Configuration mechanism
* Parameter evaluation (planned)
* Logging (planned)

Create and load environment

        virtualenv -p /usr/bin/python2.7 venv    # First time only
        source venv/bin/activate

Update dependencies

        pip install -r requirements.txt

Run all tests

        nosetests -v
