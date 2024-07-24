#!/usr/bin/env python

import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.github.johan_mi.edit")
        GLib.set_application_name("edit")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="edit")
        text_view = Gtk.TextView()
        text_view.show()
        window.add(text_view)
        window.present()

def main():
    app = MyApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)

if __name__ == "__main__":
    main()
