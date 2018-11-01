from django.db import models

# 1. Model 작성
class SearchResult(models.Model):
    keyword = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}({})'.format(self.keyword, self.search_date)
        # "어벤져스(2018.05.01)"

class Movie(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.URLField() # == CharField(max_length=200)
    release_date = models.DateField()
    search_result = models.ForeignKey(
        SearchResult,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}({})'.format(self.name, self.release_date)