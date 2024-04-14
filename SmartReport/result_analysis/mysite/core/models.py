from django.db import models
from django.views import generic


class Result(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='results/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)


class AnalysisFile(models.Model):
    title = models.CharField(max_length=100)
    excel = models.FileField(upload_to='analysis/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.excel.delete()
        super().delete(*args, **kwargs)