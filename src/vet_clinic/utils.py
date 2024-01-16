from django.conf import settings


class DataMixin:
    title = None

    def get_mixin_context(self, context, **kwargs):
        context['title'] = self.title
        context['default_service'] = settings.DEFAULT_USER_IMAGE
        context.update(**kwargs)
        return context


