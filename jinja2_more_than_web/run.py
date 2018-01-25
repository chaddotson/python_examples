#!/usr/bin/env python

from os.path import dirname, join
from jinja2 import Environment, FileSystemLoader

# http://jinja.pocoo.org/docs/2.10/templates/

templates_path = join(dirname(__file__), "templates")
templating_environment = Environment(loader=FileSystemLoader(templates_path),
                                     lstrip_blocks=True,
                                     trim_blocks=True)

template = templating_environment.get_template("pirates.jinja2")

pirates_and_ships = [
    dict(captain="Blackbeard", ship="Queen Anne's Revenge"),
    dict(captain="William Kidd", ship="Adventure Galley")
]

print(template.render(pirates=pirates_and_ships))

