from django.db import models
import uuid


class Polls(models.Model):
    name = models.CharField(max_length=50)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Questions(models.Model):
    text = models.TextField(max_length=200)
    poll = models.ForeignKey(Polls, related_name='name_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Questions, related_name='type_choice_set', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answers(models.Model):
    id_user = models.UUIDField(default=uuid.uuid4, editable=False)
    poll = models.ForeignKey(Polls, related_name='polls', on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, related_name='questions', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE)
    answer = models.TextField(max_length=100, null=True)