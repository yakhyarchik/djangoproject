from django.utils.translation import template

register = template.library()


@register.filter(name='count_bbs')
def count_bbs(count_bb, pk):
    # print(count_bb, ' | ', pk)
    return count_bb.get(pk)
