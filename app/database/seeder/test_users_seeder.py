from app.settings.database import SessionLocal
from app.models.user import UserOrm
from app.settings.env import Env

# シードデータ
test_users = [
    {"firebase_uid": Env.TEST_USER1_FIREBASE_UID, "name": "test_user1", "email": "test1@test.com", "password": "hashed_password1"},
    {"firebase_uid": Env.TEST_USER2_FIREBASE_UID, "name": "test_user2", "email": "test2@test.com", "password": "hashed_password2"},
    {"firebase_uid": Env.TEST_USER3_FIREBASE_UID, "name": "test_user3", "email": "test3@test.com", "password": "hashed_password3"},
    {"firebase_uid": Env.TEST_USER4_FIREBASE_UID, "name": "test_user4", "email": "test4@test.com", "password": "hashed_password4"},
]

def test_users_seeder():
    for test_user in test_users:
        with SessionLocal.begin() as db:
            existing_test_user = db.query(UserOrm).filter_by(name=test_user["name"]).first()
            if not existing_test_user:
                db.add(UserOrm(**test_user))
            db.commit()
            
test_users_seeder()

