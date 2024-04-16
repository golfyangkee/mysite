import csv
import datetime
from django.contrib import admin
from .models import User
from django.http import HttpResponse
from django.utils import timezone

# Register your models here.



def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv', charset='euc-kr')
    response['Content-Disposition'] = 'attachment;filename={}.csv'.format(opts.verbose_name)

    # 원래 response에 파일이 들어가야 한다. 이 자체도 파일
    writer = csv.writer(response)

    fields = [field for field in modeladmin.list_display if field not in ('password',)]
    # fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    # csv 헤더
    writer.writerow([modeladmin.model._meta.get_field(field).verbose_name.title() for field in fields])
    # writer.writerow([field.verbose_name for field in fields])

    # 실제 데이터
    for obj in queryset:
        data_row=[]
        for field in fields:
            value = getattr(obj, field)
            # value = getattr(obj, field.name)
            if isinstance(value, timezone.datetime): # datetime.datetime
                value=value.strftime("%Y-%m-%d") # 원하는 양식 지정
            data_row.append(value)
        writer.writerow((data_row))
    return response

# 보여질 때 이름
export_to_csv.short_description = 'Export_to_CSV'


class UserAdmin(admin.ModelAdmin):
    list_display =['username','birthday','gender','date_joined',]
    list_filter = []
    actions=[export_to_csv]

# admin에 만든 유저 등록
admin.site.register(User, UserAdmin)

