from .models import Question

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(post_save, sender=Question)
def createQuestion(sender, instance, created, **kwargs):
    if (created):   # if created
        question = instance
        question.order = Question.objects.all().count()
        question.updateDelay
        question.save()