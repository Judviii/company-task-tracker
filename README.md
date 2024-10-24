# Company task tracker
"Tracking your tasks, powering your productivity"
Task Tracker Service, specified for IT company.
## Check it out!

[ Company task tracker project deploy to Render](https://company-task-tracker.onrender.com)

## Installation
### Prerequisites

Before you can run this project, make sure you have the following installed:

- Python 3.11 or higher
- Django 4.1
- pip (Python package installer)

### Running the app with Python
```shell
git clone https://github.com/Judviii/company-task-tracker.git
cd company_task_tracker

# on macOS
python3 -m venv venv
source venv/bin/activate
# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
# Change the SECRET_KEY variable in settings.py 
# to run it locally.
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver # Starts Django server

(App will be available at http://127.0.0.1:8000/)
python manage.py test # Run test
```

## Features

+	implement login and logout functionality in the project.
+	managing tasks, task types, workers and position formats directly from website interface

### Additional data:

Please use this test login for  [ Company task tracker project deploy to Render](https://company-task-tracker.onrender.com):
+ username: Test
+ password: BFMQhzsX
