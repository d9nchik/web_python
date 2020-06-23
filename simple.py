#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
name = form.getvalue('name', 'Unknown')
print('Content-type: text/plain\n')

print('Hello, {}!'.format(name))
