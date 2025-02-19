# article model
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP
from datetime import datetime, timezone
from app.models.base import Base
import pytz

INDONESIA_TZ = pytz.timezone("Asia/Jakarta")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(Enum("News", "Article", "Event", "Tips", "Other"), nullable=False)
    status = Column(Enum("Publish", "Draft", "Trash"), nullable=False, default="Draft")
    created_date = Column(
        TIMESTAMP,
        default=lambda: datetime.now(timezone.utc).astimezone(INDONESIA_TZ),
    )
    updated_date = Column(
        TIMESTAMP,
        default=lambda: datetime.now(timezone.utc).astimezone(INDONESIA_TZ),
        onupdate=lambda: datetime.now(timezone.utc).astimezone(INDONESIA_TZ),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category,
            "status": self.status,
            "created_date": self.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_date": self.updated_date.strftime("%Y-%m-%d %H:%M:%S"),
        }
