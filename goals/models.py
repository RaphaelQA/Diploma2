from django.db import models

from todolist.models import BaseModel
from core.models import User


# Create your models here.
# USER = get_user_model


class GoalCategory(BaseModel):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    objects = models.Manager()
class Goal(BaseModel):

    class Status(models.IntegerChoices):
        to_do = 1, 'To do'
        in_progress = 2, 'In progress'
        done = 3, 'Done'
        archived = 4, 'Archived'

    class Priority(models.IntegerChoices):
        low = 1, 'Low'
        medium = 2, 'Medium'
        high = 3, 'High'
        critical = 4, 'critical'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(GoalCategory, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.to_do)
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, default=Priority.medium)

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

    def __str__(self):
        return self.title

    objects = models.Manager()

class GoalComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

    objects = models.Manager()
