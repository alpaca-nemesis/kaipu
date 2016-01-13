from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class artical(models.Model):
	title = models.CharField(u'title',max_length=80)
	content = UEditorField(u'content ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	abstract = UEditorField(u'abstract ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	tag = models.CharField(u'tag',max_length=20)
	slug = models.CharField(u'slug', max_length=256, db_index=True)

	def __unicode__(self):
		return self.title


class message(models.Model):
	name = models.CharField(u'name',max_length=50)
	mail = models.CharField(u'mail',max_length=30)
	phone = models.CharField(u'phone',max_length=30)
	content = UEditorField(u'content ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	abstract = UEditorField(u'abstract ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	
	def __unicode__(self):
		return self.name

class product(models.Model):
	name = models.CharField(u'name',max_length=50)
	abstract = UEditorField(u'abstract ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	content = UEditorField(u'content ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	tag = models.CharField(u'tag',max_length=20)
	slug = models.CharField(u'slug', max_length=256, db_index=True)

	def __unicode__(self):
		return self.name

class news(models.Model):
	name = models.CharField(u'name',max_length=50)
	abstract = UEditorField(u'abstract ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	content = UEditorField(u'content ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	time = models.DateTimeField(u'time')

	def __unicode__(self):
		return self.name

class certif(models.Model):
	name = models.CharField(u'name',max_length=50)
	abstract = UEditorField(u'abstract ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	content = UEditorField(u'content ',width=600, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":12040000})
	time = models.DateTimeField(u'time')
	
	def __unicode__(self):
		return self.name
