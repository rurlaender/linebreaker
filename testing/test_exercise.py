from lib.linebreaker import Exercise

def test_Exercise_01():
    exe = Exercise("A test exercise","",5,8,10,5,4,90)
    test_str = '{"description": "", "leftHand": 5, "offTime": 5, "onTime": 10, "pause": 90, "repetitions": 4, "rightHand": 8, "title": "A test exercise"}'
    assert exe.toJSON(indent=None) == test_str

def test_Exercise_02():
    exe = Exercise("Another test exercise","Short description",1,2,3,4,5,6)
    test_str = '{"description": "Short description", "leftHand": 1, "offTime": 4, "onTime": 3, "pause": 6, "repetitions": 5, "rightHand": 2, "title": "Another test exercise"}'
    assert exe.toJSON(indent=None) == test_str
