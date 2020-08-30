import datetime

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter

from notice.models import Notice
from django.contrib import admin
from django.db.models import Q


class DateFilter(SimpleListFilter):
    title = _('Filter ')

    parameter_name = 'date'

    def lookups(self, request, model_admin):
        return (
            ('new', _('new')),
            ('old', _('old')),
            ('24', _('24')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'new':
            return queryset.filter(pub_date__range=(datetime.date(2020, 1, 1), (datetime.date(2021, 1, 1)))).order_by(
                'pub_date').reverse()
        elif self.value() == 'old':
            return queryset.filter(pub_date__range=(datetime.date(2020, 1, 1), (datetime.date(2021, 1, 1)))).order_by(
                'pub_date', 'name')
        elif self.value() == '24':
            return queryset.filter(pub_date__date=datetime.datetime.now())
        else:
            return queryset


class InputFilter(admin.SimpleListFilter):
    template = 'notice/imput_filter.html'

    def lookups(self, request, model_admin):
        return (
            ('name', _('Name')),
        )


class UIDFilter(InputFilter):
    parameter_name = 'name'
    title = _('Name')

    def queryset(self, request, queryset):
        if self.value() is not None:
            uid = self.value()
            return queryset.filter(
                Q(name=uid)
            )


class PageAdmin(admin.ModelAdmin):
    list_filter = [DateFilter, UIDFilter]
    list_display = ['name', 'email', 'pub_date', 'image']
    ordering = ['pub_date']


class Meta:
    model = Notice


admin.site.register(Notice, PageAdmin)
# admin.site.register(Notice)
# admin.site.unregister(Group)
