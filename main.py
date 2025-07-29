from grade_calculator import GradeCalculator

def main():
    """This is basically the main function to run the Grade Generator Calculator application."""
    try:
        print("\n" + "*" * 55)
        print("WELCOME TO THE GRADE GENERATOR CALCULATOR ")
        print("*" * 55)
        print("\nThis application helps you calculate your course grade based on:")
        print("• Individual assignment grades and weights")
        print("• Formative and Summative category performance")
        print("• GPA calculation (on a scale of 0 to 5.0)")
        print("• Pass/Fail determination")
        print("\n" + "-" * 55)
        
        # Create calculator instance and run
        calculator = GradeCalculator()
        calculator.collect_input()
        calculator.show_results()
        
        print("\n" + "*" * 55)
        print("Thank you for using the Grade Generator Calculator!")
        print("*" * 55)
        
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Kindly restart the application and try again.")

if __name__ == "__main__":
    main()


