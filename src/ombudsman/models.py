from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from cpf_field.models import CPFField
from model_utils.models import TimeStampedModel

class Interaction(TimeStampedModel):
    entry = models.ForeignKey('Entry', verbose_name=_('entry'), on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, null=True, blank=True, verbose_name=_("author"), on_delete=models.CASCADE)
    attachment = models.FileField(
        _('attachment'), upload_to='ombudsman/interaction/', blank=True)
    internal_memo = models.TextField(_('internal memo'))
    public_memo = models.TextField(_('public memo'))

    class Meta:
        verbose_name = _('Interaction')
        verbose_name_plural = _('Interactions')
        ordering = ['-created']

    def __str__(self):
        return "{0}".format(self.name)

class EntryStatus(TimeStampedModel):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _('Entry Status')
        verbose_name_plural = _('Entrys Status')

    def __str__(self):
        return "{0}".format(self.name)

class EntryType(TimeStampedModel):
    name = models.CharField(_('name'), max_length=255)
    color = models.CharField(_('color'), max_length=20, blank=True)
    icon = models.CharField(_('icon'), max_length=100, blank=True)

    class Meta:
        verbose_name = _('Entry Type')
        verbose_name_plural = _('Entrys Type')

    def __str__(self):
        return "{0}".format(self.name)

class EntrySource(TimeStampedModel):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _('Entry Source')
        verbose_name_plural = _('Entrys Source')

    def __str__(self):
        return "{0}".format(self.name)
        
class EntryTopic(TimeStampedModel):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _('Entry Topic')
        verbose_name_plural = _('Entrys Topic')

    def __str__(self):
        return "{0}".format(self.name)

class Entry(TimeStampedModel):
    VISIBILITY_CHOICES = (
        ('anonimous', _('I don\'t want identify myself')),
        ('public', _('I want indentify myself'))
    )

    GENDER_CHOICES = (        
        ('not-answer', _('Not answer')),
        ('female', _('Female')),
        ('male', _('Male'))
    )

    AGE_GROUP_CHOICES = (
        ('up to 18 years', 'até 18 anos'),
        ('18 to 24 years', '18 a 24 anos'),
        ('25 to 34 years', '25 a 34 anos'),
        ('35 to 44 years', '35 a 44 anos'),
        ('45 to 54 years', '45 a 54 anos'),
        ('55 to 64 years', '55 a 64 anos'),
        ('more than 65 years', 'mais de 65 anos')
    )

    received = models.DateTimeField(
        _('received'), default=None, blank=True, null=True)
    source = models.ForeignKey('EntrySource', verbose_name=_(
        'Source'), blank=True, default=None, null=True, on_delete=models.CASCADE)
    entry_type = models.ForeignKey('EntryType', verbose_name=_('Type'), on_delete=models.CASCADE)
    visibility = models.CharField(
        _('visibility'), default='public', choices=VISIBILITY_CHOICES, max_length=255)
    name = models.CharField(_('name'), blank=True, max_length=255)
    cpf = CPFField(null=True,default=None)
    phone = PhoneNumberField(_('phone'), null=True, default=None)
    district = models.CharField(_('district'), blank=True, max_length=255)
    gender = models.CharField(
        _('gender'), choices=GENDER_CHOICES, max_length=255, default='', blank=True)
    age_group = models.CharField(
        _('age group'), choices=AGE_GROUP_CHOICES, blank=True, max_length=255)
    subject = models.CharField(_('subject'), max_length=255)
    protocol = models.CharField(_('protocol'), blank=True, max_length=255)
    message = models.TextField(_('message'))
    email = models.EmailField(_('email'), blank=True, max_length=255)
    topic = models.ForeignKey(
        'EntryTopic', default=None, null=True, verbose_name=_('topic'), on_delete=models.CASCADE)
    assigned = models.PositiveIntegerField(
        _('assigned'), blank=True, null=True, default=None)
    status = models.ForeignKey('EntryStatus', verbose_name=_(
        'status'), default=None, null=True, on_delete=models.CASCADE)
    answer = models.TextField(_('answer'), blank=True)
    answer_file = models.FileField(
        _('answer file'), upload_to='ombudsman/answer/', blank=True)
    answer_file_label = models.CharField(
        _('answer file label'), blank=True, max_length=255)

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entrys')
        ordering = ['-modified']

    def __str__(self):
        return "{0}".format(self.name)

class Attachment(TimeStampedModel):
    entry = models.ForeignKey('Entry', verbose_name=_('entry'), on_delete=models.CASCADE)
    archive = models.FileField(_('archive'), upload_to='ombudsman/entry/')

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')

    def __str__(self):
        return "{0}".format(self.archive.url)