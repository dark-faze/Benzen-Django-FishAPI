# Fish Api Bezen

Fish Api is made using Django and Pillow to resize images.
Has 3 endpoints :

/addRecord : (POST) Will add the data.

/getAllRecords : (GET) Will show all the records in descending order by latest.

/getRecord : (GET) Will get all the records matching key and value.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies.

```bash
pip install Django
pip install djangorestframework
pip install Pillow
```
## Setup
Run the following :

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Demo Video
Click on this [link](https://youtu.be/UcgRcmHLUA0) to watch the demo.
