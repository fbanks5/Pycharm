import random

# Expanded trivia questions dictionary
trivia_questions = {
    "Movies": [
        {"question": "Who directed the movie 'Inception'?", "answer": "Christopher Nolan"},
        {"question": "Which movie won the Oscar for Best Picture in 2020?", "answer": "Parasite"},
        {"question": "What is the highest-grossing film of all time?", "answer": "Avengers: Endgame"},
        {"question": "Who played Jack Dawson in 'Titanic'?", "answer": "Leonardo DiCaprio"},
        {"question": "Which movie features the quote 'I'll be back'?", "answer": "The Terminator"}
    ],
    "TV Shows": [
        {"question": "What is the name of the coffee shop in 'Friends'?", "answer": "Central Perk"},
        {"question": "Who played Walter White in 'Breaking Bad'?", "answer": "Bryan Cranston"},
        {"question": "Which TV show features the character Sheldon Cooper?", "answer": "The Big Bang Theory"},
        {"question": "In 'The Office', what is the name of Michael Scott's boss?", "answer": "Jan Levinson"},
        {"question": "What is the name of the fictional town where 'Stranger Things' is set?", "answer": "Hawkins"}
    ],
    "Plays": [
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
        {"question": "Which play features the character Willy Loman?", "answer": "Death of a Salesman"},
        {"question": "In which play does the character Blanche DuBois appear?", "answer": "A Streetcar Named Desire"},
        {"question": "Who wrote 'Waiting for Godot'?", "answer": "Samuel Beckett"},
        {"question": "Which play features the character Eliza Doolittle?", "answer": "Pygmalion"}
    ],
    "Music": [
        {"question": "Who is known as the 'Queen of Pop'?", "answer": "Madonna"},
        {"question": "What is the best-selling album of all time?", "answer": "Thriller by Michael Jackson"},
        {"question": "Who is the lead singer of the band U2?", "answer": "Bono"},
        {"question": "Which artist released the album '25'?", "answer": "Adele"},
        {"question": "Who sang 'Purple Rain'?", "answer": "Prince"}
    ],
    "Books": [
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
        {"question": "What is the name of the wizarding school in 'Harry Potter'?", "answer": "Hogwarts"},
        {"question": "Who is the author of 'The Great Gatsby'?", "answer": "F. Scott Fitzgerald"},
        {"question": "Who wrote '1984'?", "answer": "George Orwell"},
        {"question": "What is the name of the main character in 'The Catcher in the Rye'?",
         "answer": "Holden Caulfield"}
    ],
    "Video Games": [
        {"question": "What is the best-selling video game of all time?", "answer": "Minecraft"},
        {"question": "Who is the main character of the 'Legend of Zelda' series?", "answer": "Link"},
        {"question": "What year was the first 'Super Mario Bros.' game released?", "answer": "1985"},
        {"question": "In 'Fortnite', what is the name of the in-game currency?", "answer": "V-Bucks"},
        {"question": "Which game features a battle royale mode called 'Warzone'?", "answer": "Call of Duty"}
    ],
    "Comics": [
        {"question": "Who created the character Spider-Man?", "answer": "Stan Lee and Steve Ditko"},
        {"question": "Which comic book company publishes 'Batman'?", "answer": "DC Comics"},
        {"question": "What is the real name of Iron Man?", "answer": "Tony Stark"},
        {"question": "Who is the author of the 'Sandman' series?", "answer": "Neil Gaiman"},
        {"question": "Which superhero team includes members like Cyclops and Wolverine?", "answer": "X-Men"}
    ],
    "Sports": [
        {"question": "Which country won the FIFA World Cup in 2018?", "answer": "France"},
        {"question": "Who has won the most NBA championships as a player?", "answer": "Bill Russell"},
        {"question": "In which sport would you perform a slam dunk?", "answer": "Basketball"},
        {"question": "Who holds the record for the most home runs in a single MLB season?", "answer": "Barry Bonds"},
        {"question": "Which tennis player has won the most Grand Slam titles?", "answer": "Serena Williams"}
    ]
}


def ask_question(category):
    questions = trivia_questions[category]
    question = random.choice(questions)
    user_answer = input(f"{question['question']} ")
    if user_answer.strip().lower() == question['answer'].strip().lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {question['answer']}.")


def main():
    categories = list(trivia_questions.keys())
    print("Welcome to the Trivia Game!")
    print("Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    try:
        choice = int(input("Select a category by entering the corresponding number: "))
        if 1 <= choice <= len(categories):
            selected_category = categories[choice - 1]
            print(f"You selected {selected_category}. Let's start!")
            ask_question(selected_category)
        else:
            print("Invalid choice. Please select a valid category number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
