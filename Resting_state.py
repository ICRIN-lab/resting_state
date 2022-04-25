
from psychopy import core
from screeninfo import get_monitors

from task_template import TaskTemplate

screen = get_monitors()[0]
width = screen.width
height = screen.height


class RestingState(TaskTemplate):
    yes_key_name = "p"
    yes_key_code = "p"
    no_key_code = "a"
    no_key_name = "a"
    quit_code = "q"
    good_luck = ""
    keys = ["space", yes_key_name, no_key_name, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    def
    instructions = [
        f"Avant de commencer les tâches cognitives, nous allons faire un exercice de relaxation."]
    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False):
        self.create_visual_text(f"Vous allez garder vos yeux fermés pendant 5 min.").draw()
        self.win.flip()
        core.wait(5)
        self.create_visual_text(f"La seule consigne: Gardez les yeux fermés jusqu'à ce que l'instructeur vous demande de les rouvrir.").draw()
        self.win.flip()
        core.wait(5)
        self.create_visual_text(f"C’est parti, fermez vos yeux et détendez vous.").draw()
        self.win.flip()
        core.wait(5)
        self.create_visual_image(image=f'img/img_fond_noir.png', size=(width, height)).draw()
        self.win.flip()
        core.wait(3)#à chaner en 5*60=300
        self.create_visual_text(f"Nous allons continuer la période de relaxation. Vous allez garder les yeux ouverts et fixer la croix pendant 5 minutes.").draw()
        self.win.flip()
        core.wait(7)
        self.create_visual_text(f"Fixez la croix jusqu'à sa disparition et détendez vous. Essayez de cligner des yeux le moins possible.").draw()
        self.win.flip()
        core.wait(7)
        self.create_visual_image(image=f'img/img_croix_blanche.png', size=(width, height)).draw()
        self.win.flip()
        core.wait(3)#à chaner en 5*60=300
        self.create_visual_text("L'exercice de relaxation est à présent terminé. Merci!").draw()
        self.win.flip()
        core.wait(10)
        exit()
exp = RestingState(csv_folder="csv")
exp.start()
