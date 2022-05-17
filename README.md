# Resting State Task 

## CONTENTS OF THIS FILE

* Introduction
* Resting State Task
* Requirements
* Contributions
* More informations
* Contact


## INTRODUCTION

Our research team is studying different aspects of psychiatric disorders. Our present project is all about exploring obssessive compulsive disorders' secret garden. For that matter, we designed original home-made cognitive tasks, fresh out of the oven!

## Resting State Task

Sorry to disappoint you, but nothing is happening in this task. But we are interested in YOU doing absolutely nothing, can you imagine that ?!

More seriously, the resting a state in a standard task that is widely studied in neuroimaging for instance. 

This is the first task of the experiment. It is kind of a *"me time"* before the hard work begins. Indeed, the subject is asked to follow some instructions to close his/her eyes for 5 minutes and open them for 5 minutes. 

The instructions are written in french, and are designed for "Trackpad" response.


## REQUIREMENTS

### Imports :

We use the package PsychoPy under Python 3.6 to run the tasks. Furthermore, Resting State Task requires the import of time, as the time spent by the participants is a valuable data.
```python
from psychopy import core
from screeninfo import get_monitors
import time
from Template_Task_Psychopy.task_template import TaskTemplate
```

In order to import TaskTemplate, here are our recommendations. :

* **Step 1** : Clone Template_Task_Psychopy repository from GitHub 


Here's the <a href="https://github.com/ICRIN-lab/Template_Task_Psychopy.git"> link </a>


* **Step 2**: Create a symbolic link locally with Template_Task_Psychopy :

```python
  yourtask_directory % ln -s ../Template_Task_Psychopy Template_Task_Psychopy
```  



### Specificities :

If you want to try this cognitive task using your keyboard, don't forget to the response_pad to False

```python
class RestingState(TaskTemplate):
    response_pad = False  # has to be set on "True" if a trackpad is used.
```

## Contributions

To contribute, please fork the repository, hack in a feature branch, and send a pull request.

## More informations

Homepage: [iCRIN Lab](http://icrin.fr/)

## Contact us

Mail : contact@icrin.fr
Twitter : https://twitter.com/RedwanMaatoug
