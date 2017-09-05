# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.files.storage import FileSystemStorage


fsq = FileSystemStorage(location='/media/')
fsa = FileSystemStorage(location='/media/')
fsr = FileSystemStorage(location='/media/')


# Create your models here.

class ExamPaper(models.Model):
    SEMESTER_CHOICES = (
        ('ONE', '1'),
        ('TWO', '2'),
        ('THREE', '3')
    )
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SUBMITTED', 'Submitted'),
        ('LATE', 'Late'),
        ('FORWARDED', 'Forwarded'),
        ('APPROVED', 'Approved')
    )
    examPaperQuestion = models.FileField(storage=fsq, blank=True, null=True)
    examPaperAnswers = models.FileField(storage=fsa, blank=True, null=True)
    examPaperReport = models.FileField(storage=fsr, blank=True, null=True)
    year = models.IntegerField()
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    # paperTimeStamp =
    # solutionTimeStamp =
    # reportTimeStamp =
    notes = models.CharField(max_length=100, default="")


class MembershipExamUser(models.Model):
    id = models.AutoField(primary_key=True)
    examPaper = models.ForeignKey(ExamPaper)
    firstExaminer = models.ForeignKey('accs.UserProfile', related_name='primary')
    secondExaminer = models.ForeignKey('accs.UserProfile', related_name='secondary')
    externalExaminer = models.ForeignKey('accs.UserProfile', related_name='tertiary')

    # def __str__(self):
    #        	return '%s' % (self.firstExaminer.username)