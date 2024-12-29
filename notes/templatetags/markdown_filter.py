from django import template
import markdown2
import pygments

register = template.Library()

@register.filter
def markdown_to_html(text):
    return markdown2.markdown(text, extras=["fenced-code-blocks"])
