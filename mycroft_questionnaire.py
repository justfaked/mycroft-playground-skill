import os
import json


class questionnaire:
    def __init__(self, skill_triggered, utterance):
        self.skill = skill_triggered
        self.utterance = utterance
        self.survey = []

    def ask_and_save(self, skill, number):
        question = self.get_question(number)
        answer = skill.ask_yesno(question)
        self.survey.append((self.utterance[0], question, answer))

    def skill_interaction_response(self):
        self.ask_and_save(1)
        self.ask_and_save(2)
        # self.speak_dialog(str(self.survey))
        survey_copy = self.survey.copy()
        with open(os.path.join(self.skill.root_dir, 'log_file_ours.json'), 'w') as f:
            json.dump(survey_copy, f, indent=4, sort_keys=True)

    def get_question(number):
        question = {1: "Do you know you lost private information?",
                    2: "In your opinion which information got lost?"}
        return question[number]
