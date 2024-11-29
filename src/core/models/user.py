from sqlalchemy.orm import mapped_column, Mapped
from core.db.base import Base
import uuid as uuid_pkg


class User(Base):
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(nullable=False)

    uuid: Mapped[uuid_pkg.UUID] = mapped_column(
        primary_key=True, unique=True, default=uuid_pkg.uuid4, nullable=True
    )
    disabled: Mapped[bool] = mapped_column(nullable=False, default=True)
    superuser: Mapped[bool] = mapped_column(nullable=False, default=False)
