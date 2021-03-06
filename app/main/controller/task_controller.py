from flask import request
from flask_restplus import Resource

from ..utils.dto_objects import TaskDto
from ..logic.task_service import *

api = TaskDto.api
_task = TaskDto.task


@api.route('/api/v1/')
class TaskCreateIndex(Resource):
    @api.doc('Retorna todas as tarefas')
    @api.marshal_list_with(_task, envelope='data')
    def get(self):
        """
        Retorna todas as tarefas registradas no banco (index/read)
        """
        return index_task()

    @api.response(201, 'Tarefa criada com sucesso')
    @api.doc('Cria tarefas via')
    @api.expect(_task, validation=True)
    def post(self):
        """
        Cria nova tarefa (create)
        """
        data = request.json
        return create_task(data=data)


@api.route('/api/v1/<task_id>')
@api.param('task_id', 'Identificacão da tarefa')
@api.response(404, 'Task not found')
class TaskWithParam(Resource):

    @api.doc('Atualiza tarefa')
    @api.expect(_task, validade=True)
    def patch(self, task_id):
        """
        Atualiza dados da tarefa (update)
        """
        data = request.json
        task = show_task(idTarefa=task_id)

        if not task:
            api.abort(404)
            return "Task don't exists"
        else:
            return update_task(idTarefa=task_id, data=data)

    @api.doc('Deletar tarefa')
    def delete(self, task_id):
        """
        Deletar tarefa via idTarefa (delete)
        """
        task = show_task(idTarefa=task_id)

        if not task:
            api.abort(404)
            return "Task don't exists"
        else:
            return delete_task(idTarefa=task_id)

    @api.doc('Mostrar apenas uma tarefa')
    @api.marshal_with(_task)
    def get(self, task_id):
        """
        Buscar tarefa especifico (show)
        """

        task = show_task(idTarefa=task_id)
        if not task:
            api.abort(404)
        else:
            return task


@api.route('api/v1/status/<task_id>')
@api.param('task_id', 'Identificacão da tarefa')
@api.response(404, 'Task not found')
class TaskStatus(Resource):

    @api.doc('Verificar status de uma tarefa')
    def get(self, task_id):
        """
        Retorna status da tarefa
        """
        task = show_task(idTarefa=task_id)
        if not task:
            api.abort(404)
        else:
            return get_status(idTarefa=task_id)


@api.route('/api/v1/user/<task_id>')
@api.param('task_id', 'Identificacão da tarefa')
@api.response(404, 'User not found')
class TaskUser(Resource):

    @api.doc('Retorna ids das tarefas em que o usuario esta')
    def get(self, task_id):
        """
        Retorna id dos usuario desse tarefa

        Args:
            self (class.self):
            task_id (id do tarefa):

        """
        task = show_task(idTarefa=task_id)

        if not task:
            api.abort(404)
            return "task don't exists"
        else:
            return index_userTask(idTarefa=task_id)

    @api.doc('Finaliza tarefa, adicionando creditos ao usuario')
    @api.response(201, 'Tarefa finalizada com sucesso')
    @api.expect(_task, validation=True)
    def post(self, task_id):
        """
        Atualiza o status da tarefa e adiciona creditos ao usuario

        Args:
            self (class.self):
            task_id (id referente a tarefa):

        """
        task = show_task(idTarefa=task_id)
        data = request.json

        if not task:
            api.abort(404)
            return "task don't exists"
        else:
            return finish_task(idTarefa=task_id, data=data)
