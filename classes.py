class ExerciseSession:
    def __init__(self, exercise, intensity, duration=0):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration

    def  get_exercise(self):
        return self.exercise
    def get_intensity(self):
        return self.intensity
    def get_duration(self):
        return self.duration

    def set_exercise(self, new_exercise):
        self.exercise = new_exercise
    def set_intensity(self, new_intensity):
        self.intensity = new_intensity
    def set_duration(self, new_duration):
        self.duration = new_duration

    def calories_burned(self):
        if self.intensity == "Low":
            return 4 * self.duration
        elif self.intensity == "Moderate":
            return 8 * self.duration
        elif self.intensity == "High":
            return 12 * self.duration
        else:
            return "You must proveide valid intensity"


new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())
