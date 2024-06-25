from app.database.seeder import muscle_groups_seeder, test_users_seeder, exercises_seeder

def run_seeders():
  muscle_groups_seeder()
  test_users_seeder()
  exercises_seeder()
