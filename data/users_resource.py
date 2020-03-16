from flask import jsonify
from data import db_session
import datetime
from flask_restful import reqparse, abort, Resource
from data.users import User


def abort_if_news_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        news = session.query(User).get(user_id)
        return jsonify({'users': news.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
                  'modified_date'))})

    def delete(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        news = session.query(User).get(user_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
                  'modified_date')) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        d0, d1, d2 = [int(i) for i in args['modified_date'].split('-')]
        news = User(
            id=args['id'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            modified_date=datetime.date(d0, d1, d2)
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)
parser.add_argument('modified_date', required=True)
