from lib.linebreaker import Exercise

def test_Exercise_01():
    exe = Exercise("A test exercise","",5,8,10,5,4,90)
    test_str = '{\n    "description": "",\n    "leftHand": 5,\n    "offTime": 5,\n    "onTime": 10,\n    "pause": 90,\n    "repetitions": 4,\n    "rightHand": 8,\n    "title": "A test exercise"\n}'
    assert exe.toJSON() == test_str

def test_Exercise_02():
    exe = Exercise("Another test exercise","Short description",1,2,3,4,5,6)
    test_str = '{\n    "description": "Short description",\n    "leftHand": 1,\n    "offTime": 4,\n    "onTime": 3,\n    "pause": 6,\n    "repetitions": 5,\n    "rightHand": 2,\n    "title": "Another test exercise"\n}'
    assert exe.toJSON() == test_str
