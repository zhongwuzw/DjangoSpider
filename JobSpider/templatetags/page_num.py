from django import template

register = template.Library()

def showPageNum(page_obj):
    temp = page_obj.paginator.num_pages if page_obj.paginator.num_pages < 3 else 3
    temp_li = [t + page_obj.number for t in range(temp) if t + page_obj.number <= page_obj.paginator.num_pages ]
    return {"page_list":temp_li}

register.inclusion_tag('show_page_num.html')(showPageNum)