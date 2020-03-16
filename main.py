from flask import Flask
from flask_restful import Api
from data import db_session
from data import users_resource
from data import jobs_resource

app = Flask(__name__)
api = Api(app)
db_session.global_init("db/blogs.sqlite")
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')
url = 'http://127.0.0.1:00/'

if __name__ == '__main__':
    app.run()