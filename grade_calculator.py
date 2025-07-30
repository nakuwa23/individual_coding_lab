from assignment import Assignment

class GradeCalculator:
    """
    This is the main calculator class that tackles assignment collection, validation,
    and grade calculations including GPA and Pass/Fail determination.
    """
    def __init__(self):
        """Initialize the calculator with empty assignment lists and category trackers."""
        self.assignments = []
        self.total_weight = {'Formative': 0, 'Summative': 0}
        self.weighted_grades = {'Formative': 0, 'Summative': 0}

    def validate_category(self, category):
        """Check that the category is either Formative or Summative."""
        valid_categories = ['Formative', 'Summative']
        return category in valid_categories

    def validate_weight(self, category, weight):
        """Check that the weight is positive and doesn't exceed the remaining category limit."""
        if weight <= 0 or weight > 100:
            return False
        # Check if adding this weight would exceed 100% for the category
        return self.total_weight[category] + weight <= 100

    def validate_grade(self, grade):
        """Check that the grade is within the acceptable range (0-100)."""
        return 0 <= grade <= 100

    def get_valid_input(self, prompt, validator, error_msg):
        """A method to get valid input with error handling."""
        while True:
            try:
                user_input = input(prompt).strip()
                if validator(user_input):
                    return user_input
                else:
                    print(f"Error: {error_msg}")
            except (ValueError, KeyboardInterrupt):
                print(f"Error: {error_msg}")

    def collect_input(self):
        print("\nPlease enter your assignment info. You can key in multiple assignments.")
        print("Valid Categories: Formative or Summative \n")
        
        while True:
            print("\n" + "=" * 55)
            print("NEW ASSIGNMENT ENTRY")
            print("=" * 55)
            
            # Get assignment name with validation
            while True:
                name = input("Enter assignment name: ").strip()
                if name:
                    break
                print("Error: Assignment name cannot be blank!")

            # Get category with validation         
            while True:
                print("\nSelect category:")
                print("1. Formative")
                print("2. Summative")
                choice = input("Enter choice (1/2): ").strip()
                
                if choice == '1':
                    category = 'Formative'
                    break
                elif choice == '2':
                    category = 'Summative'
                    break
                else:
                    print("Error: Please enter choice 1 or 2 only.")

            # Get weight with validation
            while True:
                try:
                    remaining_weight = 100 - self.total_weight[category]
                    print(f"\nRemaining weight available in {category} category: {remaining_weight}%")
                    weight = float(input("Enter assignment weight (as %): "))
                    
                    if not self.validate_weight(category, weight):
                        if weight <= 0:
                            print("Error: Weight must be greater than 0!")
                        elif weight > 100:
                            print("Error: Weight cannot exceed 100%!")
                        else:
                            print(f"Error: Weight exceeds remaining limit! Maximum allowed: {remaining_weight}%")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid weight number!")

            # Get grade with validation
            while True:
                try:
                    grade = float(input("Enter the grade obtained (0-100%): "))
                    if not self.validate_grade(grade):
                        print("Error: Grade must be between 0 and 100!")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid grade number!")

            # Create and add assignment
            assignment = Assignment(name, category, weight, grade)
            self.assignments.append(assignment)
            self.total_weight[category] += weight
            self.weighted_grades[category] += assignment.weighted_grade

            print(f"\nAssignment '{name}' added successfully!")
            print(f"Category: {category} | Weight: {weight}% | Grade: {grade}%")

            # Prompt for more assignments
            while True:
                more = input("\nWould you like to add another assignment? (y/n): ").strip().lower()
                if more in ['y', 'yes', 'n', 'no']:
                    break
                print("Error: Please enter 'y' for yes or 'n' for no")
            
            if more in ['n', 'no']:
                break

    def calculate_gpa(self):
        """Calculate GPA out of 5.0 based on total weighted scores."""
        total_weighted_score = self.weighted_grades['Formative'] + self.weighted_grades['Summative']
        gpa = (total_weighted_score / 100) * 5
        return round(gpa, 2)

    def calculate_category_averages(self):
        """Calculate average grades for each category based on weights."""
        formative_avg = 0
        summative_avg = 0
        
        # Calculate weighted average for Formative category
        if self.total_weight['Formative'] > 0:
            formative_avg = self.weighted_grades['Formative'] / self.total_weight['Formative'] * 100
        
        # Calculate weighted average for Summative category  
        if self.total_weight['Summative'] > 0:
            summative_avg = self.weighted_grades['Summative'] / self.total_weight['Summative'] * 100
            
        return round(formative_avg, 2), round(summative_avg, 2)

    def determine_pass_fail(self):
        """Determine pass/fail status based on category averages as per requirements."""
        formative_avg, summative_avg = self.calculate_category_averages()
        
        # Calculate overall average of both categories
        overall_avg = (formative_avg + summative_avg) / 2
        
        # Passmark criteria       
        if formative_avg >= 50 and summative_avg >= 50:
            return "PASS", formative_avg, summative_avg, overall_avg
        else:
            return "FAIL & REPEAT", formative_avg, summative_avg, overall_avg

    def show_results(self):
        """Display comprehensive results including all calculations and final determination."""
        print("\n" + "=" * 55)
        print("GRADE CALCULATION RESULTS")
        print("=" * 55)
        
        # Summary of the assignment
        print("\nASSIGNMENT SUMMARY:")
        print("-" * 55)
        if not self.assignments:
            print("No assignments entered.")
            return
            
        for i, assignment in enumerate(self.assignments, 1):
            print(f"{i:2d}. {assignment}")

        # Category Totals
        print("\nCATEGORY TOTALS:")
        print("-" * 55)
        print(f"Formative Total Weighted Score: {self.weighted_grades['Formative']:.2f}%")
        print(f"Summative Total Weighted Score: {self.weighted_grades['Summative']:.2f}%")
        
        # Category Averages
        formative_avg, summative_avg = self.calculate_category_averages()
        print(f"\nFormative Average: {formative_avg:.2f}%")
        print(f"Summative Average: {summative_avg:.2f}%")

        # GPA Calculation
        print("\nGPA CALCULATION:")
        print("-" * 55)
        gpa = self.calculate_gpa()
        total_score = self.weighted_grades['Formative'] + self.weighted_grades['Summative']
        print(f"Total Weighted Score: {total_score:.2f}%")
        print(f"GPA: {gpa} / 5.00")

        # Pass/Fail Determination
        print("\nRESULTs:")
        print("-" * 55)
        result, f_avg, s_avg, overall_avg = self.determine_pass_fail()
        print(f"Overall Average: {overall_avg:.2f}%")
        print(f"\nFormative Performance: {f_avg:.2f}%")
        print(f"Summative Performance: {s_avg:.2f}%")
        print(f"\nFINAL REPORT: {result}")
        
        if result == "PASS":
            print("Bravo! You have successfully passed the course!")
        else:
            print("You need to retake the course. There's always a room for improvement.")
