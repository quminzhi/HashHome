from django.db import models
import uuid

# Create your models here.
class Interest(models.Model):
    COLOR_TYPE = (
        ('#ff689b', 'pink'),
        ('#e9bf06', 'yellow'),
        ('#3fcdc7', 'light-blue'),
        ('#41cf2e', 'green'),
        ('#d6ff22', 'light-green'),
        ('#4680ff', 'blue')
    )
    ICON_TYPE = (
        ('basketball-ball', 'basketball'),
        ('book', 'book'),
        ('file-alt', 'file'),
        ('tachometer-alt', 'tachometer'),
        ('globe-americas', 'global'),
        ('clock', 'clock')
    )
    
    title = models.CharField(max_length=200)
    color = models.CharField(
        max_length=36, choices=COLOR_TYPE, default='#3fcdc7')
    icon = models.CharField(max_length=36, choices=ICON_TYPE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Work(models.Model):
    TAG_TYPE = (
        ('app', 'app'),
        ('service', 'could service'),
        ('notebook', 'notebook'),
    )
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=36, null=True,
                           blank=True, choices=TAG_TYPE)
    image = models.ImageField(
        null=True, blank=True, upload_to='portfolio/', default="portfolio/design0.jpg")
    short_intro = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Question(models.Model):
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True, default=1)
    delay = models.IntegerField(null=True, blank=True, default=100)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.order)

    class Meta:
        ordering = ['order']
    
    @property
    def updateDelay(self):
        self.delay = self.order * 100
        return self


class Developer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='team/', default="team/minzhi.png")
    github = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    webpage = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
