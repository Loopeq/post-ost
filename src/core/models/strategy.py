from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped
from core.db.base import Base
import uuid as uuid_pkg


class Strategy(Base):
    __tablename__ = "strategies"

    uuid: Mapped[uuid_pkg.UUID] = mapped_column(
        default=uuid_pkg.uuid4, nullable=True, index=True, unique=True
    )
    name: Mapped[str]
    user_uuid: Mapped[uuid_pkg.UUID] = mapped_column(
        ForeignKey("users.uuid"), index=True
    )

    __table_args__ = (
        UniqueConstraint(
            "user_uuid", "name", name="uq_strategies_names_user_ids"
        ),
    )
