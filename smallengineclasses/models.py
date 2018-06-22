from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class SmallEngineClass(models.Model):
    host = models.CharField(max_length=2000)
    street_address = models.CharField(max_length=2000)
    city = models.CharField(max_length=2000)
    session_1_date = models.DateTimeField()
    session_2_date = models.DateTimeField()

    def __str__(self):
        self.session_1_date
        return "%s (ID: %s), %s & %s " %(self.city, self.pk, self.format_time(self.session_1_date), self.format_time(self.session_2_date))

    def format_time(self, obj):
        time = obj+timedelta(hours=-6)  #weirdly strftime seems to add 6 hours onto the time...
        time = time.strftime("%a, %b %d at %I %p")
        return time

    def students_in_class(self):
        return Student.objects.filter(smallengineclass=self).count()

    def slots_left(self):
        num = self.students_in_class()
        slots = "Slots left: "
        if num == 8:
            slots += "Full"
        elif num <= 4:
            slots = ""
        else:
            slots += "%s" % (8-num)

        return slots

    class Meta:
        verbose_name_plural = "Small Engine Classes"

class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    class_updates = models.BooleanField(default=False, verbose_name='Receive updates on new classes?')
    smallengineclass = models.ForeignKey('SmallEngineClass', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
