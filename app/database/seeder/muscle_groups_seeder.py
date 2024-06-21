# seed.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.settings.database import SessionLocal
from app.models.muscle_group import MuscleGroup

# シードデータ
muscle_groups = [
    {"name": "Chest"},
    {"name": "Back"},
    {"name": "Shoulders"},
    {"name": "Legs"},
    {"name": "Arms"},
    {"name": "Abs"},
    {"name": "Glutes"},
    {"name": "Calves"}
]

def muscle_groups_seeder():
    for muscle_group in muscle_groups:
        with SessionLocal.begin() as db:
            existing_muscle_group = db.query(MuscleGroup).filter_by(name=muscle_group["name"]).first()
            if not existing_muscle_group:
                db.add(MuscleGroup(**muscle_group))
            try:
                db.commit()
            # 重複エントリが検出された場合はロールバック
            except IntegrityError:
                db.rollback()
                print("Error: Duplicate entry detected. Rolling back changes.")

muscle_groups_seeder()

