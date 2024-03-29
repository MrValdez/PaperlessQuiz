import random
import config_loader
import questions_loader

config = config_loader.get()
questions = questions_loader.get()

def generate_test_paper():
    total_questions = min(len(questions), config["Total Questions"])

    if config["Question Random Order"]:
        test_paper = random.sample(questions, total_questions)
    else:
        test_paper = questions[:total_questions]

    # grab one correct answer and add in the wrong answers. then randomize the order.
    # grab the image and question.
    for i, question in enumerate(test_paper):
        correct_answers = question[3]
        wrong_answers = question[4]
        correct_answer = random.choice(correct_answers)
        answers = [correct_answer]
        
        total_answers = max(1, min(len(wrong_answers), config["Wrong Answers per Question"]))
        if config["Answer Random Order"]:
            answers += random.sample(wrong_answers, total_answers)
        else:
            answers += wrong_answers[:total_answers]

        random.shuffle(answers)
        test_paper[i] = {
            "Image": question[0],
            "Question": question[1],
            "Answers": answers,
            "Correct Answer": correct_answer
        }

    return test_paper