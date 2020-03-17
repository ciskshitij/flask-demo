"""Add subscription service code versions table

Revision ID: 3fca3a5b1ab0
Revises: 49952fde9c90
Create Date: 2020-03-17 06:16:20.996868

"""
from alembic import op
from datetime import datetime, timezone
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3fca3a5b1ab0'
down_revision = '49952fde9c90'
branch_labels = None
depends_on = None


def populate_subscriptions_service_code_versions(subscriptions_service_code_versions):
    op.bulk_insert(subscriptions_service_code_versions, [
        {
            'service_code_id': 1,
            'subscription_id': 2,
            'action': 'added',
            'date': datetime(2019, 9, 2, tzinfo=timezone.utc),
        }
    ])

def upgrade():
    subscriptions_service_code_versions = op.create_table('subscriptions_service_code_versions',
        sa.Column('subscription_id', sa.Integer(), nullable=False),
        sa.Column('service_code_id', sa.Integer(), nullable=False),
        sa.Column('action', sa.String(length=50), nullable=False),
        sa.Column('date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['service_code_id'], ['service_codes.id'], ),
        sa.ForeignKeyConstraint(['subscription_id'], ['subscriptions.id'], ),
        sa.PrimaryKeyConstraint('subscription_id', 'service_code_id')
    )
    populate_subscriptions_service_code_versions(subscriptions_service_code_versions)


def downgrade():
    op.drop_table('subscriptions_service_code_versions')
