"""Corrigindo relacionamento entre Transaction e Subcategory e permitindo exclusão de Subcategory sem deletar Transactions

Revision ID: bb72e075cab3
Revises: 6e1acbba3585
Create Date: 2025-03-02 05:17:10.030889

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bb72e075cab3"
down_revision: Union[str, None] = "6e1acbba3585"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 🔹 Corrigir o relacionamento entre Transaction e Subcategory
    op.drop_constraint(
        "transactions_subcategory_id_fkey", "transactions", type_="foreignkey"
    )
    op.create_foreign_key(
        "transactions_subcategory_id_fkey",
        "transactions",
        "subcategories",
        ["subcategory_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    # 🔹 Reverter a alteração da Foreign Key, voltando ao comportamento anterior
    op.drop_constraint(
        "transactions_subcategory_id_fkey", "transactions", type_="foreignkey"
    )
    op.create_foreign_key(
        "transactions_subcategory_id_fkey",
        "transactions",
        "subcategories",
        ["subcategory_id"],
        ["id"],
    )
