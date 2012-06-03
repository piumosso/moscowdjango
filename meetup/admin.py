# -*- coding: utf-8 -*-
from django.contrib import admin
from meetup.models import Talk, Sponsor, Speaker, Event


def oembed_presentation(obj):
    return bool(obj.presentation_data)
oembed_presentation.short_description = u'Слайды'
oembed_presentation.boolean = True


def oembed_video(obj):
    return bool(obj.video_data)
oembed_video.short_description = u'Видео'
oembed_video.boolean = True


class TalkAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'speaker', oembed_presentation, oembed_video, 'event']
    list_filter = ['event']
    readonly_fields = ['presentation_data', 'video_data']


class EventAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'date']


class SpeakerAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Talk, TalkAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Sponsor, SpeakerAdmin)