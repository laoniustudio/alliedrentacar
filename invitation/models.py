from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

# Create your models here.
class Invitation(models.Model):
  email = models.EmailField()
  code = models.CharField(max_length=20)

  def __unicode__(self):
    return u'%s, %s' % (self.sender.username, self.email)

  def send(self):
      subject = 'Allied DamageID'
      link = 'http://%s/invitation/accept/%s/' % (
          settings.SITE_HOST,
          self.code
      )
      template = get_template('invitation/invitation_email.txt')
      context = Context({
          'link': link,
      })
      message = template.render(context)
      send_mail(
          subject, message,
          settings.DEFAULT_FROM_EMAIL, [self.email]
      )