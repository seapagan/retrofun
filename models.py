from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db import Model


class Product(Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    manufacturer: Mapped[str] = mapped_column(String(64))
    year: Mapped[int]
    country: Mapped[str] = mapped_column(String(32))
    cpu: Mapped[str] = mapped_column(String(32))

    def __repr__(self):
        return f'Product({self.id}), "{self.name}"'
