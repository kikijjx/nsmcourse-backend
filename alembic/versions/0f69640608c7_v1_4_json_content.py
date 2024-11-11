"""v1_4_json_content

Revision ID: 0f69640608c7
Revises: 7d33e02655fb
Create Date: 2024-11-11 15:02:53.476081

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f69640608c7'
down_revision: Union[str, None] = '7d33e02655fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Добавляем явное преобразование типа данных
    op.execute('ALTER TABLE themes ALTER COLUMN content TYPE JSON USING content::json')


def downgrade() -> None:
    # В случае отката, снова меняем тип на TEXT
    op.execute('ALTER TABLE themes ALTER COLUMN content TYPE TEXT')
