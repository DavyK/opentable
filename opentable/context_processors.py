__author__ = 'davidkavanagh'

from itertools import chain
from operator import attrgetter
from characters.models import Character
from writeups.models import Writeup, Comment, SessionSummary
from campaigns.models import Campaign



from opentable.forms import LoginForm


def add_sidebar_data(request):

    recent_chars = Character.objects.order_by('-date_added')[:5]
    recent_wups = Writeup.objects.order_by('-date_added')[:5]
    recent_comms = Comment.objects.order_by('-date_added')[:5]
    recent_summs = SessionSummary.objects.order_by('-date_added')[:5]
    recent_camps = Campaign.objects.order_by('-date_added')[:5]

    # date, item type, item name

    recent = sorted(
        chain(
            recent_chars,
            recent_wups,
            recent_comms,
            recent_summs,
            recent_camps
        ), key=attrgetter('date_added')
    )
    recent_items = []
    for i in recent:

        url_string = ''

        if i.__class__.__name__ == 'Character':
            url_string = 'characters:show_character'

        elif i.__class__.__name__ == 'Writeup' or i.__class__.__name__ == 'Comment':
            url_string = 'writeups:show_writeup'

        elif i.__class__.__name__ == 'SessionSummary':
            url_string = 'writeups:show_summary'

        elif i.__class__.__name__ == 'Campaign':
            url_string = 'campaigns:show_campaign'

        recent_items.append((i._meta.verbose_name, url_string, i))

    data = {
        'navbar_login_form': LoginForm(),
        'recent_items': recent_items
    }

    return data