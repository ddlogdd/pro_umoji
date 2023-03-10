from django.db import models


from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('info_update_detail',  args=[str(self.id)])
        

class Wsf(models.Model):
    title = models.CharField(max_length=200)
    wsf_prayers = models.TextField()
    wsf_outline = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('wsf_update_detail', args=[str(self.id)])

class Kap(models.Model):
    title = models.CharField(max_length=200)
    prayers = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('kap_update_detail', args=[str(self.id)])

class ServiceReport(models.Model):
    body = models.TextField()
    Income_report = models.TextField()
    message_title = models.CharField(max_length=40)
    service_sequence = models.IntegerField()
    number_of_males = models.IntegerField()
    number_of_females = models.IntegerField()
    number_of_children = models.IntegerField()
    number_of_first_timers = models.IntegerField()
    number_of_new_converts = models.IntegerField()
    number_of_cars = models.IntegerField()
    Total_attendace = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE, 
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('ushers_update_detail', args=[str(self.id)])

class ManagementReport(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    Income_report = models.TextField()
    service_unit = models.CharField(max_length=40)
    message_title = models.CharField(max_length=40)
    service_sequence = models.IntegerField()
    number_of_males = models.IntegerField()
    number_of_females = models.IntegerField()
    number_of_children = models.IntegerField()
    number_of_first_timers = models.IntegerField()
    number_of_new_converts = models.IntegerField()
    number_of_cars = models.IntegerField()
    Total_attendace = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('cmc_update_detail', args=[str(self.id)])   

class WsfLeaders(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    wsf_centre_name = models.CharField(max_length=40)
    number_of_males = models.IntegerField()
    number_of_females = models.IntegerField()
    number_of_children = models.IntegerField()
    number_of_first_timers = models.IntegerField()
    number_of_new_converts = models.IntegerField()
    Total_attendace = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('wsfleaders_update_detail', args=[str(self.id)])  

class Media(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    testifier_name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('media_update_detail', args=[str(self.id)])

class Church(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    total_sunday_attendance = models.IntegerField()
    avg_sunday_attendance = models.IntegerField()
    avg_adults = models.IntegerField()
    avg_children = models.IntegerField()
    avg_chop = models.IntegerField()
    avg_wsf = models.IntegerField()
    no_of_wsf = models.IntegerField()
    bfc = models.IntegerField()
    highest_sunday_attendance = models.IntegerField()
    first_timers = models.IntegerField()
    new_converts = models.IntegerField()
    Total_income = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('church_update_detail', args=[str(self.id)])  
