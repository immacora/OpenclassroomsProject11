# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/2.3.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    The tests were performed using [pytest](https://pypi.org/project/pytest/) and [pytest-mock](https://pypi.org/project/pytest-mock/).
    To run all tests with details, type: `pytest -v`
    To run one module tests with details (ex. models), type: `pytest -v tests/unit_tests/test_models.py`

    To generate a test report with [coverage](https://pypi.org/project/coverage/), type: `coverage report -m` or `coverage html`

    The performance tests were performed using [locust](https://pypi.org/project/locust/) and specific clubs and competitions data allowing 10 000 entries.
    To generate a performance report with [locust](https://pypi.org/project/locust/):
        run app `py runserver.py`
        got to locust directory `cd tests\performance_tests`
        type `locust`
        launch your browser at `http://localhost:8089/`
        run test with number of users: 6 and your host
   
   ![Coverage_report](https://github.com/immacora/OpenclassroomsProject11/assets/76613773/7bf2a29b-953c-441c-abe6-fbae7f00115f)
   
   ![Locust_report](https://github.com/immacora/OpenclassroomsProject11/assets/76613773/e685fef8-1678-4bf7-b400-24b99ed1c7b5)

6. PEP 8

    To generate a flake8 report, type: `flake8 --format=html --htmldir=flake-report`
