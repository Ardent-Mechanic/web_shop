import sqlalchemy
from shop_products.db_session import SqlAlchemyBase


class Prod(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    quantity = sqlalchemy.Column(sqlalchemy.String, nullable=True)
