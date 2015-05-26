import mechanize
import json


def main(user_info, form_contents):
    # Login using Mechanize
    # http://wwwsearch.sourceforge.net/mechanize/
    with open(user_info) as data_file:
        user_data = json.load(data_file)
    url = 'https://login.umd.edu/cas/login'

    browser = mechanize.Browser()
    browser.set_handle_robots(False)  # http://stackoverflow.com/questions/2846105/screen-scraping-getting-around-http-error-403-request-disallowed-by-robots-tx
    response = browser.open(url)
    browser.select_form(nr=0)

    browser.form['username'] = user_data['directory_id']
    browser.form['password'] = user_data['password']
    browser.submit()

    # Fill out the FYI UMD request form
    title = 'Do you use a wheelchair or other assistive aid to support your mobility? We need your help!'
    description = '''Our research team is studying ways to enhance online and mobile map technologies to support people with mobility impairments.

We are recruiting people with mobility impairments who are 18 years of age or older to help us design next-generation map interfaces with accessibility enhancements. Your role is to help us better understand what methods and technologies people like you currently use when planning and taking trips in your city.

The study will last between 60-90 minutes. You will be compensated $15 per hour for your time.'''


    url = 'https://www.umd.edu/fyi/index.cfm?action=NewRequest'
    response = browser.open(url)
    try:
        browser.select_form('editform')
        browser.form['title'] = title
        browser.form['description'] = description

        browser.form['types'] = ['Other']
        browser.form.find_control(id='noDate').items[0].selected = True
        browser.form['location'] = ['114']  # 114: Hornbake Library
        browser.form['audience'] = ['Public']
        browser.form['website'] = 'http://cs.umd.edu/~kotaro/mobilitystudy.html'
        browser.form['sponsorName'] = 'Kotaro Hara'
        browser.form['sponsorPhone'] = ''
        browser.form['sponsorEmail'] = 'kotaro@cs.umd.edu'
        browser.submit()
    except:
        print "Cannot open the new request page!"

    return


if __name__ == "__main__":
    user_info = '../settings.json'
    form_contents = '../form_contents.json'
    main(user_info, form_contents)
