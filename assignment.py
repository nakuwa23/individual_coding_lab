class Assignment:
    """
    Represents an individual assignment with its details and weighted grade calculation.
    """
    def __init__(self, name, category, weight, grade):
        """
        Initialize an assignment with name, category, weight, and grade.
        Automatically calculates the weighted grade contribution.
        """
        self.name = name
        self.category = category
        self.weight = weight
        self.grade = grade
        self.weighted_grade = (grade * weight) / 100

    def __str__(self):
        """Return formatted string representation of the assignment."""
        return f"{self.name} | {self.category} | Weight: {self.weight}% | Grade: {self.grade}% | Weighted: {self.weighted_grade:.2f}"
