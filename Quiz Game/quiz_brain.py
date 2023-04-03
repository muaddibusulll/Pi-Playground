class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]

        user_answer = input(
            f"Q.{self.question_number + 1}: {current_question.text}. (True/False)?: ")

        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number == len(self.questions_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if (user_answer.lower() == correct_answer.lower()):
            self.score += 1
            print("\nYou'r right !\nYou'r current score is: " +
                  str(self.score), "/", str(self.question_number + 1) + "\n")
        else:
            print("\nYou'r wrong !\nYou'r score is: " +
                  str(self.score), "/", str(self.question_number + 1) + "\nThe correct answer was: " + correct_answer + "\n")

    def get_score(self):
        return self.score
