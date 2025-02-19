# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from app.models.base import Base
import app.models.article
from faker import Faker

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def reset_database():
    db = SessionLocal()

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    try:
        seed_posts(db)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Seeder failed: {e}")
    finally:
        db.close()

    print("Database has been reset and seeded with 50 entries of data.")


def seed_posts(db):
    fake = Faker()

    posts = [
        app.models.article.Post(
            title=fake.sentence(nb_words=6),
            content=fake.paragraph(nb_sentences=10),
            category=fake.random_element(
                elements=("News", "Article", "Event", "Tips", "Other")
            ),
            status=fake.random_element(elements=("Publish", "Draft", "Trash")),
        )
        for _ in range(50)
    ]

    db.add_all(posts)
