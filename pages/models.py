from django.db import models
import datetime

NDC_TYPE = (
    ('base year emissions goal','BASE YEAR EMISSIONS GOAL'),
    ('fixed-level goal', 'FIXED-LEVEL GOAL'),
    ('base year intensity goal','BASE YEAR INTENSITY GOAL'),
    ('baseline emissions goal','BASELINE EMISSIONS GOAL'),
)

class NDC(models.Model):
    country = models.CharField(max_length=75, default='NA')
    title = models.CharField(max_length=100)
    Submission_type = models.CharField(max_length=75, choices=NDC_TYPE, default='base year emissions goal')
    Submission_date = models.DateField(blank=False, default=datetime.date.today)
    Description = models.TextField(max_length=250, blank=False, default='NA')
    NDC_Text = models.FileField(upload_to='static/', max_length=254, default='NA')
    ref_num = models.IntegerField(blank=False, default='NA')

    def __str__(self):
        return self.title
