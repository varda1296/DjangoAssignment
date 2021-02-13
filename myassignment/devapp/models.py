from django.db import models
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.TextField()

    def __str__(self):
        return "%s %s" % (self.real_name, self.tz)


class ActivityPeriods(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return "%s %s %s" % (self.User, self.start_time, self.end_time)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    activity_periods = SerializerMethodField('get_activities')

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']

    def get_activities(self, obj):
        statistics = ActivityPeriods.objects.filter(User=obj)
        return ActivitySerializer(statistics, many=True).data
