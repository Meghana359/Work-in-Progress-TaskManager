from .routes.tasks import model_get_create_task, model_post_create_task
from .routes.tasks import model_fetch_task, model_get_update_task
from .routes.tasks import model_post_update_task, model_delete_task
from .routes.users import model_get_create_user, model_post_create_user
from .routes.users import model_fetch_user, model_get_update_user
from .routes.users import model_post_update_user, model_delete_user
from flask import make_response, render_template
from flask_restx import Resource, Namespace


user_api = Namespace('user', description='User API endpoints')
task_api = Namespace('task', description='Task API endpoints')


@user_api.route('/')
@user_api.route('/hello')              # Create a URL route to this resource
class HelloWorld(Resource):            # Create a RESTful resource
	''' HOME PAGE '''
	def get(self):                     # Create GET endpoint
		return {'hello': 'world'}


@task_api.route('/createTask')
class CreateTaskForm(Resource):
    def get(self):
        return make_response(render_template("createTask.html"))

	# def post(self):
    # 		return model_post_create_task()


@task_api.route('/create', methods=['GET', 'POST'])
class CreateTask(Resource):
	''' CREATE NEW TASK '''
	def get(self):
		return model_get_create_task()
		# return make_response(render_template("createTask.html"))

	def post(self):
		return model_post_create_task()


@task_api.route('/')
@task_api.route('/<int:task_id>')
class FetchTask(Resource):
	''' FETCH TASK '''
	def get(self, task_id=-1):
		return model_fetch_task(task_id)


@task_api.route('/edit/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
	''' UPDATE TASK '''
	def get(self, task_id):
		return model_get_update_task(task_id)

	def post(self, task_id):
		return model_post_update_task(task_id)


@task_api.route('/delete/<int:task_id>', methods=['GET', 'POST'])
class DeleteTask(Resource):
	def get(self, task_id):
		return model_delete_task(task_id)


@task_api.route('/create', methods=['GET', 'POST'])
class CreateUser(Resource):
	def get(self):
		return model_get_create_user()

	def post(self):
		return model_post_create_user()


@user_api.route('/')
@user_api.route('/<int:user_id>')
class FetchUser(Resource):
	def get(self, user_id=-1):
		return model_fetch_user(user_id)


@user_api.route('/edit/<int:user_id>', methods=['GET', 'POST'])
class UpdateUser(Resource):
	def get(self, user_id):
		return model_get_update_user(user_id)

	def post(self, user_id):
		return model_post_update_user(user_id)


@user_api.route('/delete/<int:user_id>', methods=['PUT', 'DELETE'])
class DeleteUser(Resource):
	def delete(self, user_id):
		return model_delete_user(user_id)
