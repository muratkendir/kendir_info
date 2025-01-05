from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

#Create Lists model
class List(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#Create Tags model
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create Notes model
class Note(models.Model):
    NOTE_TYPES = {
        "gnrl": "General",
        "prsn": "Personal",
        "Trck": "Trick",
        }
    title = models.CharField(max_length=255)
    content = MarkdownxField(blank=True)
    type = models.CharField(max_length=15, choices=NOTE_TYPES, default='gnrl')
    pub_date = models.DateTimeField()
    expression = MarkdownxField(blank=True)
    description = MarkdownxField(blank=True)
    example = MarkdownxField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    source_url = models.URLField(max_length=511, blank=True)
    tags = models.ManyToManyField(
        Tag,
        through="Relationship",
        through_fields=("note", "tag"),
    )
    list_id = models.ForeignKey(List, models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True)

    def __str__(self):
        return self.title

    def type_name(self):
        return self.NOTE_TYPES[self.type]

    def summary(self):
        summary = markdownify(self.description)
        return summary[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y %b')

    class Meta:
       ordering = ["-pub_date"]

class Relationship(models.Model):
    RELATION_TYPES = {
        "is_related_with": "is related with",
        "is_part_of": "is part of",
        "is_similar_to": "is similar to",
        }
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    relation = models.CharField(max_length=255, choices=RELATION_TYPES)

    def __str__(self):
        relation_name = str(self.tag) + '<-->' + str(self.note)
        return relation_name