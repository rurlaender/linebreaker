from lib.linebreaker import Exercise,Workout,BaseHolds, AppData

def test_simple_data_file():
    #some exercises
    jugs = Exercise("Jugs", "A little warmup",BaseHolds.Jugs, BaseHolds.Jugs,10,5,4,15)
    four_fingers = Exercise("Four fingers 37mm", "", BaseHolds.Four_Finger_37, BaseHolds.Four_Finger_37,9,6,4,90)

    #define some workouts

    workout_01 = Workout("Workout 01","",[jugs,four_fingers])
    workout_02 = Workout("Workout 02","",[four_fingers,jugs])

    #define app data

    export = AppData(1,[workout_01,workout_02],[],[],[],[])
    
    json_str = export.toJSON(indent=None)
    assert "Workout 01" in json_str and "Workout 02" in json_str 
    assert '"LinebreakerPRO": []' in json_str
    assert '"LinebreakerAIR": []' in json_str
    assert '"LinebreakerRAIL": []' in json_str
    assert '"LinebreakerCRIMP": []' in json_str