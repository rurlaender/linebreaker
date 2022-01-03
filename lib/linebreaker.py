from typing import List
import json


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
    
    def toJSON(self) -> str:
        """Returns the exercise as a json string

        Returns:
            str: The json string
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

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
    
    def toJSON(self) -> str:
        """Returns the workout as an json string

        Returns:
            str: The json string
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)