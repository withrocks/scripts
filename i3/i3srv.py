#!/usr/bin/env python

import i3ipc

"""
Server with custom settings for i3 that are not supported via the config alone
"""


def on(i3, e):
    # Since slack and inbox live together, we want one to get bigger than the other
    # when focused. This allows the user to see some context and everything if they focus
    try:
        if ('Slack' in e.container.window_title or
                'Inbox' in e.container.window_title):
            e.container.command('resize set width 67 ppt')
    except Exception:
        pass


i3 = i3ipc.Connection()
i3.on('window::focus', on)
try:
    i3.main()
finally:
    i3.main_quit()
