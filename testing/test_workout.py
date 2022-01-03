from lib.linebreaker import Workout, Exercise, BaseHolds
import json

def test_workout_01():
    exe = Exercise("Jugs","",BaseHolds.Jugs,BaseHolds.Jugs,10,5,4,90)
    work = Workout("First workout", "A short description",[exe])
    str = '"title": "First workout"'
    assert str in work.toJSON()
    str = '"description": "A short description"'
    assert str in work.toJSON()
    str= json.dumps(json.loads(exe.toJSON()),indent=None)
    assert str in json.dumps(json.loads(work.toJSON()),indent=None)