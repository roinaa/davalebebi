class Student:
    DEFAULT_PAY = 1000
    DEFAULT_STATUS = True

    def __init__(self, first_name: str, last_name: str, age: int, grades: list):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades
        self.status = Student.DEFAULT_STATUS
        self.pay = Student.DEFAULT_PAY
        self.get_discount()

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    def get_discount(self):
        if self.age < 18:
            self.pay *= 0.8

    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_status(self) -> str:
        avg = self.calculate_average()
        if avg > 90:
            return "Excellent"
        elif avg > 70:
            return "Good"
        elif avg > 50:
            return "Average"
        else:
            self.status = False
            return "Poor"
