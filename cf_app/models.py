from django.db import models


class Answer(models.Model):
    q1 = models.IntegerField(default=0)
    q2 = models.IntegerField(default=0)
    q3 = models.IntegerField(default=0)
    q4 = models.IntegerField(default=0)
    q5 = models.IntegerField(default=0)
    q6 = models.IntegerField(default=0)
    q7 = models.IntegerField(default=0)
    q8 = models.IntegerField(default=0)
    q9 = models.IntegerField(default=0)
    q10 = models.IntegerField(default=0)

    def __str__(self):
        return f"Answer {self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10 }"
