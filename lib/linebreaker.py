from typing import List
import json

class BaseHolds:
    """Defining the holds for the LineBreakerBaseBoard
    """
    Jugs = 1
    Sloper_32_5 = 2
    Sloper_22_5 = 3
    Four_Finger_16 = 4
    Four_Finger_20 = 5
    Four_Finger_37 = 6
    Three_Finger_18 = 7
    Three_Finger_28 = 8
    Three_Finger_45 = 9
    Two_Finger_24 = 10
    Two_Finger_30 = 11
    Two_Finger_50 = 12
    Sloper_35 = 13

class Exercise:
    """Describing a single hang board exercise
    """
    title: str
    description: str
    leftHand: int
    rightHand: int
    onTime: int
    offTime: int
    repetitions: int
    pause: int

    
    def __init__(self, title: str, description: str, leftHand: int, rightHand: int, onTime: int, offTime: int, repetitions: int, pause: int) -> None:
        """Initializes a new exercise

        Args:
            title (str): The title of the exercise
            description (str): A short description
            leftHand (int): The number of the hold for the left hand
            rightHand (int): The number of the hold for the left hand
            onTime (int): The seconds to hang
            offTime (int): The seconds to rest
            repetitions (int): The number of repetitions
            pause (int): The pause in seconds before the exercise
        """
        self.title = title
        self.description = description
        self.leftHand = leftHand
        self.rightHand = rightHand
        self.onTime = onTime
        self.offTime = offTime
        self.repetitions = repetitions
        self.pause = pause
    
    def toJSON(self, indent=4) -> str:
        """Returns the exercise as a json string

        Returns:
            str: The json string
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=indent)

class Workout:
    """Describes a workout with different exercises
    """
    title: str
    description: str
    exercises: List[Exercise]

    def __init__(self, title: str, description: str, exercises: List[Exercise]) -> None:
        """Initializes a workout

        Args:
            title (str): The title of the workout
            description (str): A short description for the workout
            exercises (List[Exercise]): A list of exercises that defines the workout
        """
        self.title = title
        self.description = description
        self.exercises = exercises
    
    def toJSON(self, indent=4) -> str:
        """Returns the workout as an json string

        Returns:
            str: The json string
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=indent)

class AppData:
    """Representing the export or import data for the app
    """
    version: int
    LinebreakerBASE  : List[Workout]
    LinebreakerPRO   : List[Workout]
    LinebreakerAIR   : List[Workout]
    LinebreakerRAIL  : List[Workout]
    LinebreakerCRIMP : List[Workout]

    def __init__(self, version: int, LinebreakerBASE: List[Workout], LinebreakerPRO: List[Workout],LinebreakerAIR: List[Workout],LinebreakerRAIL: List[Workout],LinebreakerCRIMP: List[Workout]) -> None:
        self.version = version
        self.LinebreakerBASE = LinebreakerBASE
        self.LinebreakerPRO = LinebreakerPRO
        self.LinebreakerAIR = LinebreakerAIR
        self.LinebreakerRAIL = LinebreakerRAIL
        self.LinebreakerCRIMP = LinebreakerCRIMP

    def toJSON(self, indent=4) -> str:
        """Returns the workout as an json string

        Returns:
            str: The json string
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=indent)