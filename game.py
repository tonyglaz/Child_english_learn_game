import json


def load_questions():

    with open('game_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def show_field(questions):

    for category_name, category_qs_price in questions.items():
        print(category_name.ljust(10), end=" ")
        for price, question_data in category_qs_price.items():
            asked = question_data["asked"]
            if not asked:
                print(price.ljust(5), end=" ")
            else:
                print("".ljust(5), end=" ")
        print()


def parse_input(user_input):

    user_data = user_input.split(" ")
    if len(user_data) != 2:
        return False
    if not user_data[0].isalpha():
        return False
    if not user_data[1].isdigit():
        return  False

    return {"category": user_data[0], "price": user_data[1]}


def show_stats(points, correct, incorrect):
    print("У нас закончились вопросы!")
    print(" ")
    print(f"Ваш счет {points} ")
    print(f"Верных ответов: {correct}")
    print(f"Неверных ответов: {incorrect}")


def save_results_to_file(points, correct, incorrect):
    with open('results.json', 'r', encoding='utf-8') as file:
        results = json.load(file)

    results.append(
        {"points": points, "correct": correct, "incorrect": incorrect})

    with open('results.json', 'w', encoding='utf-8') as file:
        json.dump(results, file)


def print_question(question_text):
    print(f"Слово {question_text} в переводе означает...")


def main():
    questions = load_questions()
    some_q_left = True
    points, correct, incorrect = 0, 0, 0,
    q_asked=0

    while q_asked < 9:
        show_field(questions=questions)
        print("Введите категорию и цену вопроса: ")
        user_input = input().title()
        user_data = parse_input(user_input)

        if not user_data:
            print("Нет такой категории или вопроса!")
            continue

        category, price = user_data["category"], user_data["price"]
        question = questions[category][price]
        if question["asked"]:
            print("Ты уже спрашивал это!")
            continue
        print_question(question["question"])
        user_answer = input().lower()
        if user_answer == question["answer"]:
            print("Ответ верный")
            points += int(price)
            correct += 1
        else:
            print("Ответ неверный")
            points += int(price)
            incorrect += 1

        question["asked"] = True
        q_asked+=1

    show_stats(points, correct, incorrect)
    save_results_to_file(points, correct, incorrect)


if __name__ == "__main__":
    main()
