import urllib
import urllib2
import cookielib
import json

from pprint import pprint

def main():
    with open("../settings.json") as data_file:
        user_data = json.load(data_file)
    pprint(user_data["directory_id"])
    return

    <form action="/search" method="POST" id="common_login">
    	<div>
    	<input type="hidden" name="CFID" value="29916055">
    	<input type="hidden" name="CFToken" value="20721994">
    	<input type="hidden" name="name" value="common_login">
    	<input type="hidden" name="do_login" value="true">
    	</div>


        <table style="margin-left: auto; margin-right: auto;" cellpadding="20" border="1"><tbody><tr><td>
    	<table cellpadding="5">
    		<tbody><tr><th align="right">Directory ID</th>
    			<td><input type="text" autofocus="" size="32" name="uid" tabindex="1"></td></tr>
    		<tr><th align="right">Password</th>
    			<td><input type="password" size="32" name="pw" tabindex="2"></td></tr>
    		<tr><th></th>
    			<td><input type="submit" value="Login" tabindex="3"></td></tr>
    	<tr><td colspan="2">
    	<br>
    	To discover your Directory ID, use the
    	<a href="https://directory.umd.edu/cgi-bin/chpwd?searchbyumid">Search By UMID page</a>.
    	<br>
    	To set your Directory password, use the
    	<a href="https://directory.umd.edu/cgi-bin/chpwd">Password Change page</a>.
    	</td></tr></tbody></table>
    	</td></tr>
    	</tbody></table>

    </form>

    # Authentication
    # http://stackoverflow.com/questions/13925983/login-to-website-using-urllib2-python-2-7
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    opener.addheaders = [('User-agent', RedditTesting)]

    urllib2.install_opener(opener)

    authentication_url = "https://directory.umd.edu/search?student"


    name = "name field"
    data = {
        "name": name
    }

    encoded_data = urllib.urlencode(data)
    # content = urllib2.urlopen("http://www.google.com/messages.php?action=send", encoded_data)
    content = urllib2.urlopen("http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_form_submit&action=demo_form.asp")
    print content.read()
    return


if __name__ == "__main__":
    main()
