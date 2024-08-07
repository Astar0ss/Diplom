from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="img/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)


def __str__(self):
    return str(self.user)


class Question(models.Model):
    question = models.CharField(max_length=255)
    image = models.ImageField(upload_to='questions/', blank=True, null=True)
    test = models.ForeignKey('Test', related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer_text = models.TextField('Ответ в текстовом виде')
    answer_img = models.ImageField(upload_to='answers/', blank=True, null=True)
    answer_test = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text or 'Ответ с изображением'


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f" {self.user.username} - {self.test.title} - {self.score} "