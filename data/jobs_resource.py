from flask import jsonify
from data import db_session
import datetime
from flask_restful import reqparse, abort, Resource
from data.jobs import Job


def abort_if_news_not_found(job_id):
    session = db_session.create_session()
    news = session.query(Job).get(job_id)
    if not news:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_news_not_found(job_id)
        session = db_session.create_session()
        news = session.query(Job).get(job_id)
        return jsonify({'jobs': news.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))})

    def delete(self, job_id):
        abort_if_news_not_found(job_id)
        session = db_session.create_session()
        news = session.query(Job).get(job_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource (Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(Job).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
            for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        s0, s1, s2 = [int(i) for i in args['start_date'].split('-')]
        d0, d1, d2 = [int(i) for i in args['end_date'].split('-')]
        news = Job(
            id=args['id'],
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=datetime.date(s0, s1, s2),
            end_date=datetime.date(d0, d1, d2),
            is_finished=args['is_finished'],
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('id', required=True, type=int)
parser.add_argument('team_leader', required=True)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('start_date', required=True)
parser.add_argument('end_date', required=True)
parser.add_argument('is_finished', required=True, type=bool)
