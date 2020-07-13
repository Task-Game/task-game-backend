"""empty message

Revision ID: 198371046dd1
Revises: 
Create Date: 2020-07-13 20:30:47.648604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '198371046dd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Frequencia',
    sa.Column('idFrequencia', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('idFrequencia')
    )
    op.create_table('Loja',
    sa.Column('idLoja', sa.Integer(), nullable=False),
    sa.Column('dataAbertura', sa.DateTime(), nullable=False),
    sa.Column('dataFechamento', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('idLoja')
    )
    op.create_table('Raridade',
    sa.Column('idRaridade', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('recompensa', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('idRaridade')
    )
    op.create_index(op.f('ix_Raridade_recompensa'), 'Raridade', ['recompensa'], unique=False)
    op.create_table('Usuario',
    sa.Column('idUsuario', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('cargo', sa.String(length=50), nullable=True),
    sa.Column('dataCriacao', sa.DateTime(), nullable=False),
    sa.Column('codigoConfirmacao', sa.String(length=50), nullable=False),
    sa.Column('credito', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('idUsuario'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Grupo',
    sa.Column('idGrupo', sa.Integer(), nullable=False),
    sa.Column('Loja_idLoja', sa.Integer(), nullable=True),
    sa.Column('dataCriacao', sa.DateTime(), nullable=False),
    sa.Column('dataEncerramento', sa.DateTime(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['Loja_idLoja'], ['Loja.idLoja'], ),
    sa.PrimaryKeyConstraint('idGrupo')
    )
    op.create_table('Item',
    sa.Column('idItem', sa.Integer(), nullable=False),
    sa.Column('Loja_idLoja', sa.Integer(), nullable=True),
    sa.Column('Raridade_idRaridade', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Loja_idLoja'], ['Loja.idLoja'], ),
    sa.ForeignKeyConstraint(['Raridade_idRaridade'], ['Raridade.idRaridade'], ),
    sa.PrimaryKeyConstraint('idItem'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('Tarefa',
    sa.Column('idTarefa', sa.Integer(), nullable=False),
    sa.Column('Grupo_idGrupo', sa.Integer(), nullable=True),
    sa.Column('Raridade_idRaridade', sa.Integer(), nullable=True),
    sa.Column('Frequencia_idFrequencia', sa.Integer(), nullable=True),
    sa.Column('dataAbertura', sa.DateTime(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('prazo', sa.DateTime(), nullable=False),
    sa.Column('recompensa', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['Frequencia_idFrequencia'], ['Frequencia.idFrequencia'], ),
    sa.ForeignKeyConstraint(['Grupo_idGrupo'], ['Grupo.idGrupo'], ),
    sa.ForeignKeyConstraint(['Raridade_idRaridade'], ['Raridade.idRaridade'], ),
    sa.PrimaryKeyConstraint('idTarefa'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('recompensa')
    )
    op.create_table('usuario_grupo',
    sa.Column('idUsuarioGrupo', sa.Integer(), nullable=False),
    sa.Column('Usuario_idUsuario', sa.Integer(), nullable=True),
    sa.Column('Grupo_idGrupo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Grupo_idGrupo'], ['Grupo.idGrupo'], ),
    sa.ForeignKeyConstraint(['Usuario_idUsuario'], ['Usuario.idUsuario'], ),
    sa.PrimaryKeyConstraint('idUsuarioGrupo')
    )
    op.create_table('Checklist',
    sa.Column('idChecklist', sa.Integer(), nullable=False),
    sa.Column('Tarefa_idTarefa', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('feito', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['Tarefa_idTarefa'], ['Tarefa.idTarefa'], ),
    sa.PrimaryKeyConstraint('idChecklist')
    )
    op.create_table('usuario_tarefa',
    sa.Column('idUsuarioTarefa', sa.Integer(), nullable=False),
    sa.Column('Usuario_idUsuario', sa.Integer(), nullable=True),
    sa.Column('Tarefa_idTarefa', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Tarefa_idTarefa'], ['Tarefa.idTarefa'], ),
    sa.ForeignKeyConstraint(['Usuario_idUsuario'], ['Usuario.idUsuario'], ),
    sa.PrimaryKeyConstraint('idUsuarioTarefa')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario_tarefa')
    op.drop_table('Checklist')
    op.drop_table('usuario_grupo')
    op.drop_table('Tarefa')
    op.drop_table('Item')
    op.drop_table('Grupo')
    op.drop_table('Usuario')
    op.drop_index(op.f('ix_Raridade_recompensa'), table_name='Raridade')
    op.drop_table('Raridade')
    op.drop_table('Loja')
    op.drop_table('Frequencia')
    # ### end Alembic commands ###
