from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date'
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date'
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is the name of the setting.'

    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the setting.'
    )
    parameter = models.CharField(

        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='This is the parameter of the setting.'

    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name', ]


class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is the name of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the setting.'
    )
    file = models.ImageField(

        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images',

    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name', ]


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is the name of the setting.'

    )
    percentage = models.IntegerField(
        default=50,

        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],

    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['order', ]


class Capabilities(AbstractModel):
    order = models.IntegerField(default=0, verbose_name='Order')
    name = models.CharField(max_length=254, verbose_name='Title', default='')
    text = models.TextField(verbose_name='Description', default='')
    image = models.ImageField(upload_to='capabilities/', verbose_name='Image', blank=True, null=True)
    link = models.URLField(verbose_name='Link', default='https://github.com/', blank=True)

    def __str__(self):
        return f'Capabilities Setting: {self.name}'

    class Meta:
        verbose_name = 'Capability'
        verbose_name_plural = 'Capabilities Settings'
        ordering = ['name']


from django.db import models


class Message(models.Model):
    name = models.CharField(
        max_length=254,
        blank=False,
        verbose_name='Name',
        help_text='Name of the sender.'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Order',
        help_text='Ordering position for this entry.'
    )

    email = models.EmailField(
        max_length=254,
        blank=False,
        verbose_name='Email',
        help_text='Email address of the sender.'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Phone',
        help_text='Phone number of the sender (optional).'
    )
    message = models.TextField(
        blank=False,
        verbose_name='Message',
        help_text='Content of the message.'
    )

    def __str__(self):
        return f'Message: {self.name}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['order', ]
