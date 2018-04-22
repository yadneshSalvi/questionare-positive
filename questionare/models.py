from django.db import models

# Create your models here.
EMOTION_CHOICES = (
    ('1', '1 - Not at all happy'),
    ('2', '2 - Neutral'),
    ('3', '3 - Little Happy'),
    ('4', '4 - Moderately Happy'),
    ('5', '5 - Very Happy'),
)

FIGURE_CHOICES = (
    ('1', 'Circle in middle of figure A is bigger than circle in middle of figure B'),
    ('2', 'Circle in middle of figure B is bigger than circle in middle of figure A'),
    ('3', 'Both the circle in the middle are of the same size'),
)

class Response(models.Model):
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	experience = models.CharField(max_length=4000)
	emotion_scale = models.CharField(max_length=1, choices=EMOTION_CHOICES)
	ans_1 = models.CharField(max_length=30)
	ans_2 = models.CharField(max_length=1, choices=FIGURE_CHOICES)
	ans_3 = models.CharField(max_length=30)
	ans_4 = models.CharField(max_length=30)

	def __str__(self):
		return self.name
