from app.settings.database import SessionLocal
from app.models.user import UserOrm

# シードデータ
test_users = [
    {"name": "test_user1", "email": "test1@test.com", "password": "hashed_password1"},
    {"name": "test_user2", "email": "test2@test.com", "password": "hashed_password2"},
    {"name": "test_user3", "email": "test3@test.com", "password": "hashed_password3"},
]

def test_users_seeder():
    for test_user in test_users:
        with SessionLocal.begin() as db:
            existing_test_user = db.query(UserOrm).filter_by(name=test_user["name"]).first()
            if not existing_test_user:
                db.add(UserOrm(**test_user))
            db.commit()
            
test_users_seeder()

