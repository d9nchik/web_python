#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print('Content-type: text/plain\n')
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Greeting Page</title>
</head>
<body>
<h1>Hello, {}!</h1>
<form action="simple.py">Change name
<input type="submit">
</form>
</body>
</html>
""".format(name))
