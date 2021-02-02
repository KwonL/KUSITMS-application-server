from django import template

register = template.Library()


@register.simple_tag
def get_checked_from_interview_date(val, i, j, n):
    if len(val) == 0:
        return
    date_list = val.split(",")
    return "checked" if date_list[i * n + j] == "1" else ""
