from database.db import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Post(db.Model):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    image: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(String(220), nullable=False)
    user_id = mapped_column(ForeignKey("user.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.email,
            "image": self.image,
            "description": self.description,
            "user_id": self.user_id
            # do not serialize the password, its a security breach
        }
