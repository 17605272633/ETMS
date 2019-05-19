from haystack import indexes
from .models import student_table, teacher_table


class student_tableIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return student_table

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
