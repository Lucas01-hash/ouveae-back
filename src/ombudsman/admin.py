from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import (Attachment, Entry, EntryTopic, EntrySource,
EntryType, EntryStatus, Interaction)

@admin.register(EntryType)
class EntryTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(EntrySource)
class EntrySourceAdmin(admin.ModelAdmin):
    list_display = ("name",)


class AttachmentTabularInline(admin.TabularInline):
    model = Attachment
    extra = 1
    classes = ["collapse"]


class InteractionStackedInline(admin.StackedInline):
    model = Interaction
    extra = 1
    exclude = ["author"]
    readonly_fields = ("created", "author")

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        "protocol",
        "created",
        "name",
        "entry_type",
        "status",
        "is_answered",
        "get_interaction_count",
        "modified",
        "last_author",
    )
    readonly_fields = ("created", "protocol")
    fieldsets = (
        (
            _("Demand"),
            {
                "fields": (
                    "status",
                    "created",
                    "received",
                    "entry_type",
                    "topic",
                    "subject",
                    "message",
                ),
            },
        ),
        (
            _("Internal control"),
            {
                "classes": ("collapse",),
                "fields": (
                    "protocol",
                    "source",
                    "assigned",
                    "answer",
                    "answer_file",
                    "answer_file_label",
                ),
            },
        ),
        (
            _("Contact information"),
            {
                "classes": ("collapse",),
                "fields": (
                    "visibility",
                    "name",
                    "phone",
                    "email",
                    "gender",
                    "age_group",
                    "district",
                ),
            },
        ),
    )
    search_fields = ("name", "district", "subject", "email", "protocol")
    inlines = (AttachmentTabularInline, InteractionStackedInline)
    date_hierarchy = "created"

    def save_formset(self, request, form, formset, change):
        print (request.user)
        instances = formset.save(commit=False)
        for obj in instances:
            if getattr(obj, "author", None) is None:
                obj.author = request.user
                obj.save()

        formset.save_m2m()
    

admin.site.register(Attachment)
admin.site.register(EntryTopic)
admin.site.register(EntryStatus)
admin.site.register(Interaction)