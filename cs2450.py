import random

# Quiz questions
# Quiz questions with explanations
quiz_questions = [
    {
        "question": "What is the primary goal of software engineering?",
        "options": ["a) Developing software quickly", "b) Producing high-quality software that meets user requirements", "c) Creating visually appealing user interfaces", "d) Managing software projects efficiently"],
        "correct_answer": "b",
        "explanation": "The primary goal of software engineering is to produce high-quality software that meets user requirements. While efficiency and user interface design are important, the quality and meeting user needs take precedence."
    },
    {
        "question": "Which software development model follows a sequential, linear approach with distinct phases?",
        "options": ["a) Agile model", "b) Waterfall model", "c) Spiral model", "d) Iterative model"],
        "correct_answer": "b",
        "explanation": "The Waterfall model follows a sequential, linear approach with distinct phases, including planning, design, development, testing, and maintenance."
    },
    {
        "question": "What is the purpose of requirements engineering in software development?",
        "options": ["a) Designing the user interface", "b) Testing the software for bugs", "c) Identifying and documenting user needs and system requirements", "d) Deploying the software to production"],
        "correct_answer": "c",
        "explanation": "Requirements engineering involves identifying and documenting user needs and system requirements. It's a critical step in understanding what the software should achieve."
    },
    {
        "question": "Which software development methodology emphasizes individuals and interactions over processes and tools?",
        "options": ["a) Waterfall methodology", "b) Agile methodology", "c) V-model methodology", "d) Spiral methodology"],
        "correct_answer": "b",
        "explanation": "The Agile methodology emphasizes individuals and interactions over processes and tools. It values collaboration and adaptability in software development."
    },
    {
        "question": "What is the primary purpose of software testing?",
        "options": ["a) To ensure the software is bug-free", "b) To validate the software against user requirements", "c) To document the software's functionality", "d) To optimize the software for performance"],
        "correct_answer": "b",
        "explanation": "The primary purpose of software testing is to validate the software against user requirements. It ensures that the software functions as intended."
    },
    {
        "question": "Which type of software maintenance involves modifying the software to improve its performance or enhance its features?",
        "options": ["a) Corrective maintenance", "b) Adaptive maintenance", "c) Perfective maintenance", "d) Preventive maintenance"],
        "correct_answer": "c",
        "explanation": "Perfective maintenance involves modifying the software to improve its performance or enhance its features without addressing defects. It aims to make the software better."
    },
    {
        "question": "In the context of software quality assurance, what does the acronym CMMI stand for?",
        "options": ["a) Capability Maturity Model Integration", "b) Computer Maintenance and Management Information", "c) Critical Metrics for Measuring Integration", "d) Configuration Management and Maintenance Integration"],
        "correct_answer": "a",
        "explanation": "In the context of software quality assurance, CMMI stands for Capability Maturity Model Integration. It's a framework for process improvement and maturity assessment."
    },
    {
        "question": "What is the purpose of conducting a code review in software development?",
        "options": ["a) To identify and fix bugs in the code", "b) To evaluate the performance of the software", "c) To assess the code's compliance with coding standards", "d) To gather feedback from end-users"],
        "correct_answer": "c",
        "explanation": "The purpose of conducting a code review in software development is to assess the code's compliance with coding standards and best practices. It helps ensure code quality."
    },
    {
        "question": "Which diagramming technique is commonly used in software design to depict the interactions between objects?",
        "options": ["a) Use case diagram", "b) Class diagram", "c) Sequence diagram", "d) Activity diagram"],
        "correct_answer": "c",
        "explanation": "The diagramming technique commonly used in software design to depict the interactions between objects is the sequence diagram. It shows the chronological flow of messages."
    },
    {
        "question": "What is the key principle behind the agile manifesto?",
        "options": ["a) Customer collaboration over contract negotiation", "b) Comprehensive documentation over working software", "c) Following a rigid plan over embracing change", "d) Strict adherence to processes over individual interactions"],
        "correct_answer": "a",
        "explanation": "The key principle behind the agile manifesto is 'Customer collaboration over contract negotiation.' Agile emphasizes close collaboration with customers to meet their evolving needs."
    },
    {
        "question": "How does software configuration management (SCM) contribute to software development?",
        "options": ["a) It ensures that the software meets all quality standards.", "b) It tracks and controls changes made to the software during its development lifecycle.", "c) It manages the deployment and installation of the software in production environments.", "d) It optimizes the software's performance and scalability."],
        "correct_answer": "b",
        "explanation": "Software Configuration Management (SCM) contributes to software development by tracking and controlling changes made to the software during its development lifecycle. It helps maintain version control and consistency."
    },
    {
        "question": "Which of the following is not a characteristic of good software design?",
        "options": ["a) Modularity", "b) High coupling", "c) Low cohesion", "d) Reusability"],
        "correct_answer": "b",
        "explanation": "High coupling is not a characteristic of good software design. Good design aims for low coupling, which reduces interdependencies between components."
    },
    {
        "question": "What is the purpose of software testing?",
        "options": ["a) To find defects and errors in the software", "b) To ensure the software meets all requirements", "c) To verify the correctness of the software", "d) To validate the software against user expectations"],
        "correct_answer": "a",
        "explanation": "The purpose of software testing is to find defects and errors in the software. It helps identify issues that need to be fixed."
    },
    {
        "question": "What is the primary goal of the Agile software development approach?",
        "options": ["a) Detailed planning and documentation", "b) Sequential and rigid process flow", "c) Emphasizing individual interactions and adaptability", "d) Long-term project predictability and stability"],
        "correct_answer": "c",
        "explanation": "The primary goal of the Agile software development approach is to emphasize individual interactions and adaptability. Agile values collaboration and responsiveness to change."
    },
    {
        "question": "Which software development model is characterized by a series of overlapping iterations?",
        "options": ["a) Waterfall model", "b) Spiral model", "c) Agile model", "d) Incremental model"],
        "correct_answer": "b",
        "explanation": "The Spiral model is characterized by a series of overlapping iterations. It allows for flexibility and risk management throughout the development process."
    },
    {
        "question": "What is the purpose of a use case diagram in software requirements analysis?",
        "options": ["a) To identify potential software defects", "b) To visualize the flow of control in the software", "c) To model interactions between actors and the system", "d) To estimate the project schedule and cost"],
        "correct_answer": "c",
        "explanation": "The purpose of a use case diagram in software requirements analysis is to model interactions between actors (users) and the system. It helps define system functionality."
    },
]

# Flashcards
flashcards = [
    {
        "term": "Agile Methodology",
        "definition": "A software development approach that emphasizes individuals and interactions over processes and tools."
    },
    {
        "term": "Waterfall Model",
        "definition": "A sequential software development process in which progress is seen as flowing steadily downwards through phases of planning, design, development, testing, and maintenance."
    },
    {
        "term": "Software Testing",
        "definition": "The process of evaluating and verifying that a software application or system meets specified requirements and functions correctly."
    },
    {
        "term": "Code Review",
        "definition": "A systematic examination of source code intended to find and fix errors, improve code quality, and ensure compliance with coding standards."
    },
    {
        "term": "Configuration Management",
        "definition": "A discipline that helps ensure the software's functionality, performance, and other qualities meet the requirements."
    },
    {
        "term": "Refactoring",
        "definition": "The process of restructuring existing computer code without changing its external behavior to improve code quality, maintainability, and reduce technical debt."
    },
]



def take_quiz(questions):
    score = 0
    random.shuffle(questions)
    
    for idx, question in enumerate(questions, start=1):
        print(f"Question {idx}: {question['question']}")
        for option in question['options']:
            print(option)
        
        user_answer = input("Your answer (a, b, c, or d): ").strip().lower()
        if user_answer == question['correct_answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['correct_answer'].upper()}\n")
    
    print(f"You scored {score}/{len(questions)} on this quiz.")

def review_flashcards(cards):
    random.shuffle(cards)
    
    for card in cards:
        input(f"Term: {card['term']} (Press Enter to reveal definition)")
        print(f"Definition: {card['definition']}\n")

def main():
    while True:
        print("Main Menu:")
        print("1. Take Quiz")
        print("2. Review Flashcards")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            take_quiz(quiz_questions)
        elif choice == '2':
            review_flashcards(flashcards)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
