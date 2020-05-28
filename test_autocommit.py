#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mysite'))


def test():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    
    import django
    django.setup()

    
    from django import db
    from polls.models import NotAPoll

    with db.transaction.atomic():
        o = NotAPoll.objects.create(text=1)
    assert o.text == 1

    o.text = 2
    o.save()
    o.refresh_from_db()
    assert o.text == 2

    db.close_old_connections()

    # this fails unless `set autocommit=1` is added to init_command (in settings.py L84)
    # or the global mysql setting is changed
    o.refresh_from_db()
    assert o.text == 2


if __name__ == '__main__':
    test()