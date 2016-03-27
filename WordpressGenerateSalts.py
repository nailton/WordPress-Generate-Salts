import sublime, sublime_plugin, urllib.request, re

#Linux broken SSL http://sublimetext.userecho.com/topic/50801-bundle-python-ssl-module/
API_URL = "http://api.wordpress.org/secret-key/1.1/salt/"

# Extends TextCommand so that run() receives a View to modify.
class WordpressGenerateSaltsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for cursor in self.view.sel():
            salts = request_url()
            self.view.insert(edit, cursor.begin(), salts )

class WordpressSaltsDotEnvCommand(sublime_plugin.TextCommand):
    def  run(self, edit):
        for cursor in self.view.sel():
            salts = request_url()
            salts = re.sub(r"\w+\('", '', salts)
            salts = re.sub(r"',\s+", '=', salts)
            salts = re.sub(r"\);", '', salts)
            self.view.insert(edit, cursor.begin(), salts )

def request_url():
    req = urllib.request.Request(API_URL)
    response = urllib.request.urlopen(req)
    salts = response.read()
    return salts.decode("utf-8")

