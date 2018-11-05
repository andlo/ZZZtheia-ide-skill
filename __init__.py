from mycroft import MycroftSkill, intent_file_handler


class TheiaIde(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ide.theia.intent')
    def handle_ide_theia(self, message):
        self.speak_dialog('ide.theia')


def create_skill():
    return TheiaIde()

