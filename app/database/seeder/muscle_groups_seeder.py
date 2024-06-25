from app.settings.database import SessionLocal
from app.models.muscle_group import MuscleGroupOrm

# シードデータ
muscle_groups = [
    {"id": 1, "name": "胸"},
    {"id": 2, "name": "背中"},
    {"id": 3, "name": "肩"},
    {"id": 4, "name": "腕"},
    {"id": 5, "name": "お腹"},
    {"id": 6, "name": "お尻"},
    {"id": 7, "name": "脚（太もも）"},
    {"id": 8, "name": "脚（カーフ）"}
]

def muscle_groups_seeder():
    for muscle_group in muscle_groups:
        with SessionLocal.begin() as db:
            existing_muscle_group = db.query(MuscleGroupOrm).filter_by(name=muscle_group["name"]).first()
            if not existing_muscle_group:
                db.add(MuscleGroupOrm(**muscle_group))
            db.commit()

muscle_groups_seeder()

