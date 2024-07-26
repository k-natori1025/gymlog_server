from app.libraries.repositories.workout_log import WorkoutLogRepository

class CreateUserUsecase:
    def __init__(self, workout_log_repo: WorkoutLogRepository = Depends()):
        self.workout_log_repo = workout_log_repo
