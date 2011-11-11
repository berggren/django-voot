from django.contrib.auth.models import User, Group
from django.db import models
from oauth2_lite_client.models import Provider as Oauth2Provider

class VootProvider(models.Model):
    name = models.CharField(max_length=255, blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    oauth2_provider = models.ForeignKey(Oauth2Provider)
    last_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s' % self.name
    class Admin:
        pass

class VootGroup(models.Model):
    group = models.OneToOneField(Group)
    voot_id = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s' % self.provider
    class Admin:
        pass

class VootUser(models.Model):
    user = models.ForeignKey(User)
    provider = models.ManyToManyField(VootProvider)
    last_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s' % self.provider
    class Admin:
        pass

User.voot = property(lambda u: VootUser.objects.get_or_create(user=u)[0])