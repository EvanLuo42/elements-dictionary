from jinja2 import FileSystemLoader, Environment
from pyglossary import Glossary
import json

Glossary.init()

glossary = Glossary()
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('template.html')
with open('dict.json') as f:
    dictionary: list = json.load(f)

for item in dictionary.__iter__():
    glossary.addEntryObj(glossary.newEntry(
        item['symbol'],
        template.render(
            alias_name=item['symbol'],
            fullname=item['name'],
            details=item['details'],
        ),
        defiFormat='h',
    ))
    glossary.addEntryObj(glossary.newEntry(
        item['name'],
        template.render(
            alias_name=item['symbol'],
            fullname=item['name'],
            details=item['details'],
        ),
        defiFormat='h',
    ))

glossary.setInfo("title", "Elements Dictionary")
glossary.setInfo("author", "EvanLuo42")
glossary.write(filename='Elements Dictionary', format='AppleDict', css='templates/template.css')
