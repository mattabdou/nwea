# NWEA Blog API Exercise

Simple Blog API for NWEA application - a streamlined API for reading and writing blog posts through a RESTful API

### System Requirements
* Python 3.5+
* python3-venv
* git

## Installation

The Blog API requires Flask and flask_api libraries. The commands below are an example to configure and run the API from inside an empty working directory on a system that has the System Requirements installed:

```
git clone https://github.com/mattabdou/nwea.git blogapi
python3 -m venv env
source env/bin/activate
pip install Flask flask_api
```

To run the API:

```
export FLASK_APP=./blogapi/blogapi.py
flask run -h 0.0.0.0
```

You will see the Flask app init, at which point you may access the api at http://127.0.0.1:5000

```
# Get posts:
curl -X GET http://127.0.0.1:5000/posts
# Create new post:
curl -H "Content-Type: application/json" -X POST -d '{"title":"Post Title","body":"Post body"}' http://127.0.0.1:5000/post
```
