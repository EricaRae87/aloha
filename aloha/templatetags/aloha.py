# -*- coding: utf-8 -*
import random

from django import template
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _

register = template.Library()

GREETINGS = [
    ('Welcome', _('English')),
    ('Guten Tag', _('German')),
    ('Tere', _('Estonian')),
    (u'G’day', _('Australian')),
    ('Mbote', _('Lingala')),
    ('Ciao', _('Italian')),
    ('Kumusta', _('Tagalog')),
    ('Bonjour', _('French')),
    ('Salut', _('French')),
    ('Hej', _('Swedish')),
    ('Kia ora', _(u'Mäori')),
    ('Hala', _('Arabic')),
    ('Salaam', _('Arabic')),
    (u'Fáilte', _('Irish')),
    ('Ni hao', _('Mandarin')),
    ('O HAI', _('Lolspeak')),
    ('Aloha', _('Hawaiian')),
    ('Sawubona', _('Zulu')),
    (u'Përshëndetje', _('Albanian')),
    (u'Olá', _('Portuguese')),
    ('Konnichiwa', _('Japanese')),
    ('Bangawoyo', _('Korean')),
    (u'¡Hola!', _('Spanish')),
    ('Ei gude wie?', _('Hessian')),
    ('Yasou', _('Greek')),
    ('Mingalaba', _('Burmese')),
    ('Kaixo', _('Basque')),
    ('Jambo', _('Swahili')),
    ('Shalom', _('Hebrew')),
    (u'Góðan daginn', _('Icelandic')),
]

class AlohaNode(template.Node):
    """
    Updates the context with some variables and renders the greeting.
    The default variables added to the context are:
    
    aloha_language      The language
    aloha_info          A short infoline
    
    """
    def __init__(self, language='aloha_language', info='aloha_info'):
        self.language = language
        self.info = info
    
    def render(self, context):
        
        greeting, language = GREETINGS[random.randint(0, len(GREETINGS) -1)]
        infoline = _(u'Now you know how to greet people in %(language)s') % { 'language': language, }
  
        context.update({
            self.language: language,
            self.info: infoline,
        })

        return greeting

def do_aloha(parser, token):
    """
    Retrieves a random greeting and renders it, also updates 
    context with specifiied variables for further details.
    
    Syntax::
    
        {% aloha %}
        {% aloha language as [varname] and info as [varname] %}
    
    Example::
    
        {% aloha language as lang and info as tagline %}
    
    """
    
    bits = token.contents.split()
    if len(bits) == 1:
        return AlohaNode()

    if len(bits) != 8:
        raise template.TemplateSyntaxError("'%s' tag takes zero or seven arguments" % bits[0])
    if bits[2] != 'as' or bits[6] != 'as' or bits[4] != 'and':
        raise template.TemplateSyntaxError("second and seventh argument to '%s' tag must be 'as', fourth must be an 'and'" % bits[0])

    return AlohaNode(bits[3], bits[7])
    
        
register.tag('aloha', do_aloha)
