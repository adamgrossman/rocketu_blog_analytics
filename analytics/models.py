from django.db import models


class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u"{}".format(self.url)


class Location(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ['city', 'country', 'region']

    def __unicode__(self):
        return u"{}, {} {}".format(self.city, self.country, self.region)


class View(models.Model):
    location = models.ForeignKey(Location, blank=True, null=True, related_name="view")
    page = models.ForeignKey(Page, related_name="view")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return u"{} by {} @ {}".format(self.ip_address, self.location, self.timestamp)

