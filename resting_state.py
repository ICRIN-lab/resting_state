from psychopy import core
from screeninfo import get_monitors
import time
from Template_Task_Psychopy.task_template import TaskTemplate

screen = get_monitors()[0]
width = screen.width
height = screen.height


class RestingState(TaskTemplate):
    yes_key_name = "p"
    yes_key_code = "p"
    no_key_code = "a"
    no_key_name = "a"
    quit_code = "q"
    good_luck = "Vous allez garder vos yeux fermés pendant 5 minutes."
    response_pad = True
    keys = ["space", yes_key_name, no_key_name, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    instructions = [
        f"Avant de commencer les tâches cognitives, nous allons faire un exercice de relaxation."]

    def task(self, no_trial, exp_start_timestamp=False, practice=False): #trial_start_timestamp?
        #self.create_visual_text(f"Vous allez garder vos yeux fermés pendant 5 min.").draw()
        #self.win.flip()
        #self.wait_yes(False)
        self.create_visual_text(
            f"La seule consigne: gardez les yeux fermés jusqu'à ce que l'instructeur vous demande de les rouvrir.").draw()
        self.win.flip()
        self.wait_yes(self.yes_key_code)
        self.create_visual_text(f"C’est parti, fermez vos yeux et détendez vous.").draw()
        self.win.flip()
        self.wait_yes(self.yes_key_code)
        self.create_visual_image(image=f'img/img_fond_noir.png', size=(width, height)).draw()
        self.win.flip()
        core.wait(300)
        self.create_visual_text(f"Nous allons continuer la période de relaxation. Vous allez garder les yeux ouverts et"
                                f" fixer la croix pendant 5 minutes.").draw()
        self.win.flip()
        self.wait_yes(self.yes_key_code)
        self.create_visual_text(
            f"Fixez la croix jusqu'à sa disparition et détendez vous. Essayez de cligner des yeux le moins possible.").draw()
        self.win.flip()
        self.wait_yes(self.yes_key_code)
        self.create_visual_image(image=f'img/img_croix_blanche.png', size=(width, height)).draw()
        self.win.flip()
        core.wait(300)
        self.create_visual_text("L'exercice de relaxation est à présent terminé. Merci !").draw()
        self.win.flip()
        self.wait_yes(self.yes_key_code)
        exit()


exp = RestingState(csv_folder="csv")
exp.start()
