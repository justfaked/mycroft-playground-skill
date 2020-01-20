from mycroft import MycroftSkill, intent_file_handler


class MycroftPlayground(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('playground.mycroft.intent')
    def handle_playground_mycroft(self, message):
        self.speak_dialog('playground.mycroft')
        self.speak_dialog("yay hardcode!")



def create_skill():
    return MycroftPlayground()

