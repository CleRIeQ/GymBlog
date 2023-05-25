from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=150, null=False)
    preview_text = models.TextField(max_length=300, null=False)
    content = models.TextField(max_length=1500, null=False)
    date = models.DateTimeField(auto_now=True)
    preview_image = models.ImageField(upload_to="posts_images/", null=False)

    def __str__(self):
        return self.title


class PortfolioPostModel(models.Model):
    title = models.CharField(max_length=150, null=False)
    preview_text = models.TextField(max_length=300, null=False)
    preview_image = models.ImageField(upload_to="portfolio_images/", null=False)
    url = models.URLField(null=False)

    def __str__(self):
        return self.title