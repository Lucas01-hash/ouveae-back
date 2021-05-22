from django.contrib import admin
from .models import (Attachment, Entry, EntryTopic, EntrySource,
EntryType, EntryStatus, Interaction)

admin.site.register(Attachment)
admin.site.register(Entry)
admin.site.register(EntryTopic)
admin.site.register(EntrySource)
admin.site.register(EntryType)
admin.site.register(EntryStatus)
admin.site.register(Interaction)