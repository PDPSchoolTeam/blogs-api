from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    """Category model for blog posts"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tag model for blog posts"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """Blog post model"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='created_at')
    content = models.TextField()

    # Relationships
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_posts'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='blog_posts'
    )

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Status field for draft/published
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
