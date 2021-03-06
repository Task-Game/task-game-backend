import datetime
import json

from .user_service import show_user
from app.main.create_app import db
from app.main.model.main_models import TarefaTable, usuario_tarefa
from app.main.model.secondary_tables import RaridadeTable

NOW = datetime.datetime.today().strftime('%Y-%m-%d')


def create_task(data):
    """
        Criar nova task
        @param:  data = dict/json corpo da requisição enviado via post
    """
    user = show_user(data['idUsuario'])

    new_task = TarefaTable(
        Grupo_idGrupo=data['Grupo_idGrupo'],
        Frequencia_idFrequencia=data['Frequencia_idFrequencia'],
        Raridade_idRaridade=data['Raridade_idRaridade'],
        dataAbertura=NOW,
        nome=data['nome'],
        descricao=data['descricao'],
        prazo=data['prazo'],
        status=0
    )
    __save_changes(new_task)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered'
    }

    new_task.task.append(user)
    db.session.commit()

    return response_object, 201


def index_task():
    return TarefaTable.query.all()


def update_task(idTarefa, data):
    task = TarefaTable.query.filter_by(idTarefa=idTarefa).first()
    if task:
        TarefaTable.query.filter(TarefaTable.idTarefa == idTarefa).update(data)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully update'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Fail update, check the values and taskId'
        }
        return response_object, 400


def delete_task(idTarefa):
    task = TarefaTable.query.filter_by(idTarefa=idTarefa).first()
    if task:
        __delete_instance(task=task)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted'
        }
        return response_object,  200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Fail delete'
        }
        return response_object, 400


def show_task(idTarefa):
    return TarefaTable.query.filter_by(idTarefa=idTarefa).first()


def get_status(idTarefa):
    status = db.session.query(TarefaTable.status).filter(
        TarefaTable.idTarefa == idTarefa).scalar()
    return status


def index_userTask(idTarefa):
    data = dict(db.session.query(usuario_tarefa).filter_by(
        Tarefa_idTarefa=idTarefa).all())
    return data


def finish_task(idTarefa, data):
    idRaridadeTarefa = db.session.query(TarefaTable.Raridade_idRaridade).filter(
        TarefaTable.idTarefa == idTarefa
    ).scalar()

    creditos = db.session.query(RaridadeTable.recompensa).filter(
        RaridadeTable.idRaridade == idRaridadeTarefa
    ).scalar()

    task = show_task(idTarefa=idTarefa)
    user = show_user(idUsuario=data['idUsuario'])

    print("usuario:",user.credito)
    task.status = 1
    db.session.commit()

    user.credito = creditos
    db.session.commit()
    print("usuario:",user.credito)

    response_object = {
            'status': 'success',
            'message': 'Successfully Update'
        }

    return response_object


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def __delete_instance(task):
    db.session.delete(task)
    db.session.commit()
