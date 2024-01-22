from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)

  def __str__(self):
    status = ''
    if self.completed:
      status = 'Done'
    else:
      status = 'Will do'

    return f'{self.title} ({status})'

# ################################################ #
# Run: python3 manage.py makemigrations            #
# Everytime you make a change to a database model! #
# ################################################ #
