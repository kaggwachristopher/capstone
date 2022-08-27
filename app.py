from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort, jsonify
from auth import AuthError, requires_auth
from models import *
import os
from dotenv import load_dotenv

load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS setup
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/', methods=['GET'])
    def index():

        return jsonify({
            'success': True,
            'message': "Hello, welcome to my capstone project!!",
        })

    @app.route('/actors', methods=['GET'])
    @requires_auth('view:actors')
    def get_actors(payload):

        all_actors = Actor.query.order_by(Actor.id).all()

        formatted_actors = [Actor.format() for Actor in all_actors]

        if len(formatted_actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'Actors': formatted_actors,
            'total_Actors': len(formatted_actors),
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('create:actor')
    def add_actor(payload):

        body = request.get_json()

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        try:

            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()

            all_actors = Actor.query.order_by(Actor.id).all()
            formatted_actors = [Actor.format() for Actor in all_actors]

            return jsonify({
                'success': True,
            })

        except BaseException:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actor')
    def edit_actor(payload, actor_id):

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        body = request.get_json()

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        try:

            if new_name is not None:
                actor.name = new_name

            if new_age is not None:
                actor.age = new_age

            if new_gender is not None:
                actor.gender = new_gender

            actor.update()

            return jsonify({
                'success': True,
            })

        except BaseException:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        try:
            actor.delete()

        except BaseException:
            abort(422)

        return jsonify({
            'success': True,
        })

    @app.route('/movies', methods=['GET'])
    @requires_auth('view:movies')
    def get_movies(payload):

        all_movies = Movie.query.order_by(Movie.id).all()

        formatted_movies = [Movie.format() for Movie in all_movies]

        if len(formatted_movies) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'Movies': formatted_movies,
            'total_Movies': len(formatted_movies),
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('create:movie')
    def add_movie(payload):

        body = request.get_json()

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        try:
            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
            })

        except BaseException:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movie')
    def edit_movie(payload, movie_id):

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        body = request.get_json()

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        try:
            if new_title is not None:
                movie.title = new_title

            if new_release_date is not None:
                movie.release_date = new_release_date

            movie.update()

            return jsonify({
                'success': True,
            })

        except BaseException:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(movie_id):

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        try:
            movie.delete()

            return jsonify({
                'success': True,
            })

        except BaseException:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error',
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
