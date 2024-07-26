from app.settings.database import SessionLocal
from app.models.exercise import ExercisesOrm

# シードデータ
exercises = [
    {"id": 1, "name": "ベンチプレス", "muscle_group_id": 1, "is_custom": 0, "is_bodyweight": 0},
    {"id": 2, "name": "インクラインベンチプレス", "muscle_group_id": 1, "is_custom": 0, "is_bodyweight": 0},
    {"id": 3, "name": "デクラインベンチプレス", "muscle_group_id": 1, "is_custom": 0, "is_bodyweight": 0},
    {"id": 4, "name": "ダンベルフライ", "muscle_group_id": 1, "is_custom": 0, "is_bodyweight": 0},
    {"id": 5, "name": "ペックデックマシン", "muscle_group_id": 1, "is_custom": 0, "is_bodyweight": 0},
    {"id": 6, "name": "プッシュアップ", "muscle_group_id": 1, "is_custom": 0, "is_bodyweight": 1},
    {"id": 7, "name": "ケーブルクロスオーバー", "muscle_group_id": 1, "is_custom": 0, "is_bodyweight": 0},
    {"id": 8, "name": "デッドリフト", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 0},
    {"id": 9, "name": "ラットプルダウン", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 0},
    {"id": 10, "name": "バーベルロー", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 0},
    {"id": 11, "name": "シーテッドロー", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 0},
    {"id": 12, "name": "プルアップ", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 1},
    {"id": 13, "name": "チンアップ", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 1},
    {"id": 14, "name": "ワンアームダンベルロー", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 0},
    {"id": 15, "name": "Tバーロー", "muscle_group_id": 2, "is_custom": 0, "is_bodyweight": 0},
    {"id": 16, "name": "ショルダープレス", "muscle_group_id": 3, "is_custom": 0, "is_bodyweight": 0},
    {"id": 17, "name": "ダンベルショルダープレス", "muscle_group_id": 3, "is_custom": 0, "is_bodyweight": 0},
    {"id": 18, "name": "サイドレイズ", "muscle_group_id": 3, "is_custom": 0, "is_bodyweight": 0},
    {"id": 19, "name": "フロントレイズ", "muscle_group_id": 3, "is_custom": 0, "is_bodyweight": 0},
    {"id": 20, "name": "リアデルトフライ", "muscle_group_id": 3, "is_custom": 0, "is_bodyweight": 0},
    {"id": 21, "name": "アーノルドプレス", "muscle_group_id": 3, "is_custom": 0, "is_bodyweight": 0},
    {"id": 22, "name": "オーバーヘッドプレス", "muscle_group_id": 3, "is_custom": 0, "is_bodyweight": 0},
    {"id": 23, "name": "バーベルカール", "muscle_group_id": 4, "is_custom": 0, "is_bodyweight": 0},
    {"id": 24, "name": "ダンベルカール", "muscle_group_id": 4, "is_custom": 0, "is_bodyweight": 0},
    {"id": 25, "name": "トライセプスプレスダウン", "muscle_group_id": 4, "is_custom": 0, "is_bodyweight": 0},
    {"id": 26, "name": "トライセプスディップ", "muscle_group_id": 4, "is_custom": 0, "is_bodyweight": 0},
    {"id": 27, "name": "コンセントレーションカール", "muscle_group_id": 4, "is_custom": 0, "is_bodyweight": 0},
    {"id": 28, "name": "プリーチャーカール", "muscle_group_id": 4, "is_custom": 0, "is_bodyweight": 0},
    {"id": 29, "name": "スカルクラッシャー", "muscle_group_id": 4, "is_custom": 0, "is_bodyweight": 0},
    {"id": 30, "name": "クランチ", "muscle_group_id": 5, "is_custom": 0, "is_bodyweight": 1},
    {"id": 31, "name": "レッグレイズ", "muscle_group_id": 5, "is_custom": 0, "is_bodyweight": 0},
    {"id": 32, "name": "プランク", "muscle_group_id": 5, "is_custom": 0, "is_bodyweight": 0},
    {"id": 33, "name": "シットアップ", "muscle_group_id": 5, "is_custom": 0, "is_bodyweight": 1},
    {"id": 34, "name": "ロシアンツイスト", "muscle_group_id": 5, "is_custom": 0, "is_bodyweight": 1},
    {"id": 35, "name": "ケーブルクランチ", "muscle_group_id": 5, "is_custom": 0, "is_bodyweight": 0},
    {"id": 36, "name": "アブローラー", "muscle_group_id": 5, "is_custom": 0, "is_bodyweight": 1},
    {"id": 37, "name": "ヒップスラスト", "muscle_group_id": 6, "is_custom": 0, "is_bodyweight": 0},
    {"id": 38, "name": "グルートブリッジ", "muscle_group_id": 6, "is_custom": 0, "is_bodyweight": 0},
    {"id": 39, "name": "ケーブルキックバック", "muscle_group_id": 6, "is_custom": 0, "is_bodyweight": 0},
    {"id": 40, "name": "ダンベルステップアップ", "muscle_group_id": 6, "is_custom": 0, "is_bodyweight": 0},
    {"id": 41, "name": "ランジ", "muscle_group_id": 6, "is_custom": 0, "is_bodyweight": 0},
    {"id": 42, "name": "バーベルスクワット", "muscle_group_id": 6, "is_custom": 0, "is_bodyweight": 0},
    {"id": 43, "name": "スミスマシンスクワット", "muscle_group_id": 6, "is_custom": 0, "is_bodyweight": 0},
    {"id": 44, "name": "バーベルスクワット", "muscle_group_id": 7, "is_custom": 0, "is_bodyweight": 0},
    {"id": 45, "name": "レッグプレス", "muscle_group_id": 7, "is_custom": 0, "is_bodyweight": 0},
    {"id": 46, "name": "レッグエクステンション", "muscle_group_id": 7, "is_custom": 0, "is_bodyweight": 0},
    {"id": 47, "name": "レッグカール", "muscle_group_id": 7, "is_custom": 0, "is_bodyweight": 0},
    {"id": 48, "name": "ランジ", "muscle_group_id": 7, "is_custom": 0, "is_bodyweight": 0},
    {"id": 49, "name": "フロントスクワット", "muscle_group_id": 7, "is_custom": 0, "is_bodyweight": 0},
    {"id": 50, "name": "ハックスクワット", "muscle_group_id": 7, "is_custom": 0, "is_bodyweight": 0},
    {"id": 51, "name": "スタンディングカーフレイズ", "muscle_group_id": 8, "is_custom": 0, "is_bodyweight": 0},
    {"id": 52, "name": "シーテッドカーフレイズ", "muscle_group_id": 8, "is_custom": 0, "is_bodyweight": 0},
    {"id": 53, "name": "ドンキーカーフレイズ", "muscle_group_id": 8, "is_custom": 0, "is_bodyweight": 0},
    {"id": 54, "name": "カーフプレス", "muscle_group_id": 8, "is_custom": 0, "is_bodyweight": 0},
    {"id": 55, "name": "シングルレッグカーフレイズ", "muscle_group_id": 8, "is_custom": 0, "is_bodyweight": 0},
    {"id": 56, "name": "レッグプレスカーフレイズ", "muscle_group_id": 8, "is_custom": 0, "is_bodyweight": 0},
    {"id": 57, "name": "ボックスジャンプ", "muscle_group_id": 8, "is_custom": 0, "is_bodyweight": 0}
]

def muscle_groups_seeder():
    for exercise in exercises:
        with SessionLocal.begin() as db:
            existing_exercise = db.query(ExercisesOrm).filter_by(name=exercise["name"]).first()
            if not existing_exercise:
                db.add(ExercisesOrm(**exercise))
            db.commit()
           
muscle_groups_seeder()

