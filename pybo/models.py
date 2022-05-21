from django.db import models
from account.models import Account
from datetime import datetime
# 참고
# https://wikidocs.net/91424 : 이미지 업로드 관련
# https://eveningdev.tistory.com/47
# https://dheldh77.tistory.com/entry/Django-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%97%85%EB%A1%9C%EB%93%9C
# https://github.com/ForPT/ForPresenTation_Django : 경환선배 깃허브
# https://hashcode.co.kr/questions/9573/django-db-primary_key-%EC%82%AD%EC%A0%9C-%EC%A7%88%EB%AC%B8%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4
# : id pk처리 관련 Q&A
# https://ssungkang.tistory.com/entry/Django-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%A1%B0%ED%9A%8C-queryset
# : db 조건문 관련



# [이미지 파일 업로드]
# 업로드하는 이미지파일 저장 경로 설정
# 사용자이메일주소_파일이름 형태로 저장
def file_name(instance, filename):
 #   return 'files/ppts/{}_{}_{}.png'.format(instance.email, instance.image)
    return 'images/{}_{}'.format(instance.email, instance.image)
    #이미지가 이미 .jpeg 아님 jpg인데 끝이 .png인게 맞나?! 그리고 중복 데이터 마지막 변하는건 같음

# 업로드한 이미지 저장
class Image(models.Model):
    # 인덱스번호(자동으로 숫자 늘어남)
    id = models.AutoField(primary_key=True)
    # 사용자 이메일 주소
    email = models.CharField(max_length=128, verbose_name='이메일', default="")
    # 이미지 파일
    image = models.FileField(upload_to=file_name, verbose_name='이미지')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'image'
        verbose_name= '이미지업로드'
        verbose_name_plural= '이미지업로드'


#[결과값]
#체크박스 테스트 해보려고 이미지 추출된 값 저장하는 테이블 임의로 만들어봄
class Result(models.Model):
    # 이미지상 바운딩 박스의 인덱스번호(지금은 그냥 자동으로 숫자늘어나는걸로 해놓음)
    id = models.AutoField(primary_key=True)
    # 결과값 저장(딕셔너리로 저장하고 싶음)
    result = models.CharField(max_length=200)

    class Meta:
        db_table = 'Result'
        verbose_name = '추출된 값'


# [템플릿]
# 장고 어드민 페이지에서 '생성된 템플릿'이란 이름으로 만들어 놓음
# maketemplate페이지에서 '템플릿 생성'버튼 누르면 저장됨(아직 구현 X)
# templateMenu페이지에서 저장되어 있는 템플릿 목록 보여줌(구현 O)
class Template(models.Model):
    #인덱스 번호(바운딩박스의 인덱싱번호 아님/ 그냥 테이블 늘어날때 숫자 늘어나는 인덱스 번호임)
    id = models.AutoField(primary_key=True)
    #사용자 이메일
    email = models.CharField(max_length=128, verbose_name='이메일', default="")
    #대표사진
    # TemplateImage = models.FileField(upload_to=file_name, verbose_name='이미지')
    TemplateImage = models.FileField(null=True)
    #템플릿 명
    TemplateName = models.CharField(max_length=200)
    # 열이름
    # 열이름이랑 bbox의 인덱스번호를 같이 딕셔너리로 묶어서 저장하는거 시도해보려고 함
    # 그렇게 되면 지금처럼 ColumnName,User_Range이 따로 있는게 아니라 하나에다가 저장해야할꺼 같지만 우선은 그냥 둠
    # 딕셔너리로 묶어서 저장되면 그때 수정할꺼임
    ColumnName = models.CharField(max_length=200, default="")
    #사용하기
    User_Range = models.TextField(null=True)
    #그룹으로 사용하기
    User_Group = models.TextField(null=True)
    #생성일
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Template'
        verbose_name = '생성된 템플릿'



# 진섭이꺼
class Document(models.Model):
    # title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
