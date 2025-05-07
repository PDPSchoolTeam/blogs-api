from modeltranslation.translator import register, TranslationOptions
from api.models import BlogPost


@register(BlogPost)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
