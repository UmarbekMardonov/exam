from django.db import models
from django.contrib.auth import get_user_model

UserAuth = get_user_model()


# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='lesson/')
    duration = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Lesson)
    view_count = models.IntegerField(default=0)
    # users = models.ManyToManyField('auth.User')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def update_view_count(self):
        self.view_count += 1
        self.save()


class ProductSubscribers(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='subscribers')
    subscribers = models.ForeignKey(
        UserAuth, on_delete=models.CASCADE, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False)


class LessonHistory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_history')
    user = models.ForeignKey(
        UserAuth, on_delete=models.CASCADE, related_name='user_history')
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='history'
    )

    end_point = models.IntegerField()
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        if self.end_point >= .8 * self.lesson.duration:
            self.status = True


class Category(models.Model):
    title = models.CharField(max_length=220)


class Ads(models.Model):
    title = models.CharField(max_length=220)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
