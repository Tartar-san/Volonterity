from django.db import models
from django.contrib.auth.models import User, Permission, Group


# table of cities we work with
class Cities(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return "City: %s" % self.city


# types of volunteer activity
class ActivityTypes(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Type: %s" % self.name


# extending django User model with additional fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities)

    def __str__(self):
        return "Profile of %s" % str(self.user)


class Organization(models.Model):
    administrators = models.ManyToManyField(User)
    creator = models.ForeignKey(User, related_name="creator")

    def __str__(self):
        return "Organization of %s" % str(self.creator)


class OrganizationProfile(models.Model):
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=1000)

    def __str__(self):
        return "Organization: %s\nName: %s\nDescription: %s" % (str(self.organization),
                                                                self.name,
                                                                self.short_description
                                                                )


class OrganizationImages(models.Model):
    organization = models.ForeignKey(Organization)
    image = models.ImageField()
    short_description = models.CharField(max_length=300)

    def __str__(self):
        return "Organization: %s\nDescription: %s" % (str(self.organization),
                                                      self.short_description
                                                      )


class Event(models.Model):
    creator = models.ForeignKey(User)
    organization = models.ForeignKey(Organization, blank=True)
    event_types = (
        ("A", "Test A"),
        ("B", "Test B"),
    )
    title = models.CharField(max_length=100)
    city = models.ForeignKey(Cities, db_index=True)
    event_type = models.CharField(max_length=100, choices=event_types, db_index=True)
    activity_types = models.ManyToManyField(ActivityTypes)

    def __str__(self):
        return "Event: %s\nCity: %s\nType: %s\nCreator: %s" % (self.title,
                                                               str(self.city),
                                                               self.event_type,
                                                               str(self.creator)
                                                               )


class EventTimes(models.Model):
    event = models.ForeignKey(Event)
    datetime = models.DateTimeField(db_index=True)

    def __str__(self):
        return "Date: %s\nTime: %s\nEvent: %s\n" % (self.datetime.date(),
                                                    self.datetime.time(),
                                                    str(self.event)
                                                    )


class EventImages(models.Model):
    event = models.ForeignKey(Event)
    image = models.ImageField()
    short_description = models.CharField(max_length=300)

    def __str__(self):
        return "Event: %s\nDescription: %s" % (str(self.event),
                                               self.short_description
                                               )