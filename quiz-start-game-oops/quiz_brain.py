class QuizBrain:
    def __init__(self, question_list):
        print("Hello Player! your quiz starts now!!")
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        q_no = self.question_no
        current_question = self.question_list[q_no]
        print(f"Q.{q_no + 1}. {current_question.question}?:", end="")
        if input().strip().lower() == current_question.answer.lower():
            print("Nice! You got that correct\n")
            self.score += 1
        else:
            print(f"Nice Try! But the correct answer is {current_question.answer}\n")
        self.question_no += 1

    def still_has_questions(self):
        return self.question_no < len(self.question_list)
