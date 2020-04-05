from django.db import models


class DataSet(models.Model):
    date = models.DateField(null=True)
    channel = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=2, blank=True)
    os = models.CharField(max_length=128, blank=True)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    installs = models.IntegerField(default=0)
    spend = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    revenue = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)

    # @property
    # def cost_per_install(self):
    #     return self.spend / self.installs

