# Casting Agency 

  My Udacity nanodegree final project (**Capstone**)

## Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. This application aims at simplifying the streamline process.

  

#### Live API

The casting agency API is running live on heroku and can be accessed using the link below
https://chris-capstone.herokuapp.com

---

  

## Development Setup

  

#### Python 3.7

  

[Download](https://www.python.org/downloads/) and install python 3.7. Find out more about how to setup python on your computer [here ](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

  

#### Virtual Enviornment

  

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

  

#### Install Dependencies

  

Navigate into your virtual environment and run the following command. This will install the required dependencies using pip.

  

```bash

pip install -r requirements.txt

```

  

  

##### Key Dependencies

  

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

  

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

  

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

  

- [Python-Jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

  
### Create a `.env` file
This app needs a number of environment variables to be up and running

 - Create a file on the root directory named `.env`
 - Copy the contents from the `.env.example` file into your newly created `.env` file   (the default values in this file should be able to get you started but feel free to adjust them to you specific ones)

## Running the server

Navigate into your virtual environment  and run the following command

  

``` bash
flask run
```
---

  

## API Reference

  

### Authentication

  
Apart from the home route, all endpoints in this API are protected using **role based authentication**
  

#### Roles
There are 3 main roles in the Casting Agency API. 
 
 Below are the different roles with their permissions

1. **Casting Assistant :**

- view:actors

- view:movies

  

 2. **Casting Director :**

 - All permissions a Casting Assistant has

 - create:actor

 - delete:actor

 - update:actor

 - update:movie

 3. **Executive Producer :**

 - All permissions a Casting Director has

 - create:movie

 - delete:movie
---
### Fetching tokens and hitting endpoints
#### Get token
Open postman and import the collection from the file `Capstone.postman_collection.json`
- The collection has 3 directories for all the three roles.
 - Each role has a default token to help you access and test the endpoints
- Each folder also includes authentication credentials to enable you generate a new access token using implicit grant type. Generating a new token in post man will open a new window which will allow you to sign in with **google**, **github** or **email and password**
- ***Tokens should be fetched from within their folders to avoid mixup of permissions***

#### Hit endpoints
- By default the host variable in postman points to heroku change this value to your local while on development

### Error Handling

Errors are returned as JSON objects in the following format:

#### 400: Bad Request

#### 404: Resource Not Found

#### 405: Method not allowed

#### 422: Not Processable

#### 500: Internal Server Error

---

  

### Endpoints

  

#### Actors

  

-  #### GET '/actors'

- General:

- Fetch all Actor information

- Request Arguments: None

- Returns: JSON response containing all actors information, request status and the number of actors.


```json
{
"Actors": [
{
"age": 36,
"gender": "male",
"id": 1,
"name": "Summo Hung"
}
],
"success": true,
"total_Actors": 1
}
```

  

-  #### POST '/actors'

- General

- Creates a new actor

- Request Arguments: None

- Request Body: Must include name(type str), gender(type str), age(type int)
```json 
{ "name": "actor 6", "age": 19, "gender": "male" }
```

- Returns: Success value.
```
{
"success": true,
}
```

  

-  #### PATCH '/actors/int:actor_id'

- General

- edit the actor that has given

- Request Arguments: actors_id

- Request Body: name(type str), gender(type str) or age(type int)

- Returns: Success value.

```json
{
"success": true,
}
```

  

-  #### DELETE '/actors/int:actor_id'

- General:

- Deletes the actor that has given

- Request Arguments: actors_id

- Returns: Success value.

```json

{
"success": true,
}

```

  
  

#### Movies

  

-  #### GET '/movies'

- General:

- Fetch all Movies information

- Request Arguments: None

- Returns: JSON response containing all movies information, request status and the number of movies.

```json
	{
	"Movies": [
	{
	"id": 1,
	"release_date": "Sat, 15 Apr 2022 00:00:00 GMT",
	"title": "Fist of legend"
	}
	],
	"success": true,
	"total_Movies": 1
	}
```

  

-  #### POST '/movies'

- General

- Create a new movie

- Request Arguments: None

- Request Body: Must include title(type str), release_date(type datetime)
```json 
{ "title": "Tokyo drift", "release_date": "2022-01-20" }
```

- Returns: Success value.

```json
{
"success": true,
}
```

  

-  #### PATCH '/movies/int:movie_id'

- General

- edit the movie that has given

- Request Arguments: movies_id

- Request Body: title(type str), release_date(type datetime
```json
 { "title": "Fast and furious"}
```
- Returns: Success value.

```json
{
"success": true,
}
```

  

-  #### DELETE '/movies/int:movie_id'

- General:

- Deletes the movie that has given

- Request Arguments: movie_id

- Returns: Success value.

```json
{
"success": true,
}
```

## Testing

You can test the endpoint using Postman or Unittest.

  

### Unittest

  

To run the tests, run 

```bash

$ dropdb capstone_test

$ createdb capstone_test

$ psql capstone_test < capstone.psql

$ python test_app.py

```
This will create a test database and run the tests, however make sure to have the  `DATABASE_URL` to this database in your `.env` file
  

#### Postman
- Make sure you have the correct tokens for each role in your `.env`
- Run the postman collection