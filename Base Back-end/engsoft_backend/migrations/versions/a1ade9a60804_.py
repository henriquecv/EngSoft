"""empty message

Revision ID: a1ade9a60804
Revises: 
Create Date: 2019-06-12 09:03:18.842672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1ade9a60804'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alunos',
    sa.Column('num_matric', sa.BigInteger(), nullable=False),
    sa.Column('nome', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('endereco', sa.String(length=250), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('data_nascimento', sa.String(length=20), nullable=False),
    sa.Column('telefone', sa.String(length=20), nullable=False),
    sa.Column('total_horas_voo', sa.Integer(), nullable=False),
    sa.Column('concluiu_teoria', sa.String(length=3), nullable=False),
    sa.Column('concluiu_pratica', sa.String(length=3), nullable=False),
    sa.Column('data_matric', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('num_matric')
    )
    op.create_table('funcionarios',
    sa.Column('user', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('user')
    )
    op.create_table('instrutores',
    sa.Column('num_cadastro', sa.BigInteger(), nullable=False),
    sa.Column('nome', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('endereco', sa.String(length=250), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('data_nascimento', sa.String(), nullable=False),
    sa.Column('telefone', sa.String(length=20), nullable=False),
    sa.Column('breve', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('data_cadastro', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('num_cadastro')
    )
    op.create_table('voos',
    sa.Column('voo_id', sa.BigInteger(), nullable=False),
    sa.Column('data_voo', sa.String(), nullable=False),
    sa.Column('hora_inicio', sa.String(), nullable=False),
    sa.Column('horas_total', sa.Integer(), nullable=False),
    sa.Column('nota', sa.Integer(), nullable=False),
    sa.Column('instrutor_id', sa.BigInteger(), nullable=False),
    sa.Column('aluno_id', sa.BigInteger(), nullable=False),
    sa.Column('data_cadastro', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['aluno_id'], ['alunos.num_matric'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['instrutor_id'], ['instrutores.num_cadastro'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('voo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voos')
    op.drop_table('instrutores')
    op.drop_table('funcionarios')
    op.drop_table('alunos')
    # ### end Alembic commands ###
