
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import *

Casting_Assistant = os.environ['CASTING_ASSISSTANT_TOKEN']
Casting_Director = os.environ['CASTING_DIRECTOR_TOKEN']
Executive_Producer = os.environ['EXECUTIVE_PRODUCER_TOKEN']


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = os.environ['TEST_DATABASE_URL']

        setup_db(self.app, self.database_path)

        self.actor_mock = {
            "name": "Christopher Capstone",
            "age": 25,
            "gender": "male"
        }

        self.movie_mock = {
            "title": "Fist of the legend",
            "release_date": "2003-3-3"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors_for_Casting_Assistant(self):
        res = self.client().get(
            '/actors',
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_Actors'], len(data['Actors']))

    def test_get_movies_for_Casting_Assistant(self):
        res = self.client().get(
            '/movies',
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_Movies'], len(data['Movies']))

    def test_add_new_actor(self):
        res = self.client().post(
            '/actors',
            json=self.actor_mock,
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_add_new_movie(self):
        res = self.client().post(
            '/movies',
            json=self.movie_mock,
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_update_actor_age(self):
        res = self.client().patch(
            '/actors/1',
            json={
                'age': 18},
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_update_movie_title(self):
        res = self.client().patch(
            '/movies/1',
            json={
                'title': 'title is changed'},
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_delete_actor(self):  # change the id every time runing the test
        res = self.client().delete(
            '/actors/1',
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_delete_movie(self):
        res = self.client().delete(
            '/movies/1',
            headers={
                "Authorization": 'bearer ' +
                Casting_Assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_get_actors_for_Casting_Director(self):
        res = self.client().get(
            '/actors',
            headers={
                "Authorization": 'bearer ' +
                Casting_Director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies_for_Casting_Director(self):
        res = self.client().get(
            '/movies',
            headers={
                "Authorization": 'bearer ' +
                Casting_Director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_new_actor_for_Casting_Director(self):
        res = self.client().post(
            '/actors',
            json=self.actor_mock,
            headers={
                "Authorization": 'bearer ' +
                Casting_Director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_new_movie_for_Casting_Director(self):
        res = self.client().post(
            '/movies',
            json=self.movie_mock,
            headers={
                "Authorization": 'bearer ' +
                Casting_Director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_update_actor_age_for_Casting_Director(self):
        res = self.client().patch(
            '/actors/1',
            json={
                'age': 18},
            headers={
                "Authorization": 'bearer ' +
                Casting_Director})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_title_for_Casting_Director(self):
        res = self.client().patch(
            '/movies/1',
            json={
                'title': 'title is changed'},
            headers={
                "Authorization": 'bearer ' +
                Casting_Director})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_for_Casting_Director(self):
        res = self.client().delete(
            '/movies/1',
            headers={
                "Authorization": 'bearer ' +
                Casting_Director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_get_actors_for_Executive_Producer(self):
        res = self.client().get(
            '/actors',
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies_for_Executive_Producer(self):
        res = self.client().get(
            '/movies',
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_new_actor_for_Executive_Producer(self):
        res = self.client().post(
            '/actors',
            json=self.actor_mock,
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_new_movie_for_Executive_Producer(self):

        res = self.client().post(
            '/movies',
            json=self.movie_mock,
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor_age_for_Executive_Producer(self):
        res = self.client().patch(
            '/actors/1',
            json={
                'age': 18},
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_for_Executive_Producer(self):
        res = self.client().delete(
            '/actors/1',
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_title_for_Executive_Producer(self):
        res = self.client().patch(
            '/movies/1',
            json={
                'title': 'title is changed'},
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_for_Executive_Producer(self):
        res = self.client().delete(
            '/movies/1',
            headers={
                "Authorization": 'bearer ' +
                Executive_Producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


if __name__ == "__main__":
    unittest.main()
