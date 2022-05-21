from django.contrib import admin
from .models import Image, Template, Result

# 여기는 장고 어드민 페이지에서 보이는 테이블을 만들어줌
# admin페이지에 어떤 column을 관리할지 설정이 가능함

# 이미지 테이블
class ImageAdmin(admin.ModelAdmin):
    # []안에 쓰는 항목을 페이지에서 보여줌
    list_display = ['id','email', 'image']


# 템플릿 테이블
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'TemplateImage', 'TemplateName', 'ColumnName', 'User_Range', 'User_Group', 'date']

# 결과값 테이블
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'result']

# 이걸 해줘야 어드민페이지에 등록됨
admin.site.register(Image, ImageAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Result, ResultAdmin)



#site에 등록


