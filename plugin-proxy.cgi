#!/usr/bin/python
import cgi
import cgitb
import urllib2

cgitb.enable()

if __name__ == "__main__":
    form = cgi.FieldStorage()
    url = form.getvalue("url")
    if url is not None:
        url = urllib2.unquote(url)
        req = urllib2.Request(url)
        try:
            response = urllib2.urlopen(req)
            print "Content-Type: %s\r\n" % response.headers.get('Content-Type')
            print response.read()
        except:
            print "Status: 404 Not Found\r\nContent-Type: text/plain\r\n"
    else:
        print "Status: 404 Not Found\r\nContent-Type: text/plain\r\n"
