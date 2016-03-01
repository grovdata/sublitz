import os
import sublime, sublime_plugin
from blitz2 import load_mapfile, save

class TokenizeBlitzFileCommand(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if view.settings().get("enable_sublitz") == True:
            cwd = os.path.join(sublime.packages_path(), "Blitz2")
            load_mapfile(os.path.join(cwd, "tokenmap.txt"))
            region = sublime.Region(0, view.size())
            text = view.substr(region)
            #save(text, "")
