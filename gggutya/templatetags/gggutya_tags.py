from django import template
import gggutya.templates.templates_helper as th


register = template.Library()

@register.simple_tag(name='ABOUT_SITE_TAG')
def get_info_about_site():
    return th.ABOUT_SITE


@register.inclusion_tag('template_for_inclusion_tag.html', name = 'history_deals')
def get_history_deals(selected=0):
    return {'order_menu': [
                {'id': 1, 'menu': 'Сделать заказ'},
                {'id': 2, 'menu': 'Список моих заказов'},
                {'id': 3, 'menu': 'История заказов'},
            ],
            'selected': selected,
        }