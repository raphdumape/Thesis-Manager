import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'
DEFAULT_GUESTBOOK_NAME1 = 'default_guestbook1'
DEFAULT_GUESTBOOK_NAME2 = 'default_guestbook2'


# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)




class Greeting(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Guestbook(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))

class Guestbook1(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name1',
                                          DEFAULT_GUESTBOOK_NAME1)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/module-1/1?' + urllib.urlencode(query_params))

class Guestbook2(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name2',
                                          DEFAULT_GUESTBOOK_NAME2)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/module-1/2?' + urllib.urlencode(query_params))

class MemberOnePage(webapp2.RequestHandler):
    
    def get(self):
        guestbook_name = self.request.get('guestbook_name1',
                                          DEFAULT_GUESTBOOK_NAME1)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(5)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('myUserProfile.html')
        self.response.write(template.render(template_values))

class MemberTwoPage(webapp2.RequestHandler):
    
    def get(self):
        guestbook_name = self.request.get('guestbook_name2',
                                          DEFAULT_GUESTBOOK_NAME2)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(5)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('raphdumape.html')
        self.response.write(template.render(template_values))


class Thesis(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    Thesis_title = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False)
    date1 = ndb.StringProperty(indexed=False)
    status = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class ThesisNew(webapp2.RequestHandler):
    def get(self):
        
        template = JINJA_ENVIRONMENT.get_template('thesisnew.html')
        self.response.write(template.render())
    
    def post(self):
        thesis = Thesis()
        thesis.Thesis_title = self.request.get('Thesis_title')
        thesis.description = self.request.get('description')
        thesis.date1 = self.request.get('date1')
        thesis.status = self.request.get('status')
        thesis.put()
        self.redirect('/thesis/success')

class SuccessPass(webapp2.RequestHandler):
    def get(self):
        
        template = JINJA_ENVIRONMENT.get_template('Success.html')
        self.response.write(template.render())

class ThesisList(webapp2.RequestHandler):
    def get(self):

        thesisquery = Thesis.query().order(-Thesis.date).fetch()
        

        values = {
            'thesisquery': thesisquery,
        }


        template = JINJA_ENVIRONMENT.get_template('ThesisList.html')
        self.response.write(template.render(values))

class ThesisView(webapp2.RequestHandler):
    def get(self,thesis_id):
        
        thesisquery = Thesis.query().fetch()
        thesis_id = int(thesis_id)

        values = {
            'thesisquery': thesisquery,
            'id': thesis_id
        }

 
        template = JINJA_ENVIRONMENT.get_template('thesisview.html')
        self.response.write(template.render(values))

class Adviser(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    title = ndb.StringProperty(indexed=False)
    first_name = ndb.StringProperty(indexed=False)
    last_name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    pnumber = ndb.StringProperty(indexed=False)
    department = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class AdviserNew(webapp2.RequestHandler):
    def get(self):
        
        template = JINJA_ENVIRONMENT.get_template('AdviserNew.html')
        self.response.write(template.render())

    def post(self):
        adviser = Adviser()
        adviser.title = self.request.get('title')
        adviser.first_name = self.request.get('first_name')
        adviser.last_name = self.request.get('last_name')
        adviser.email = self.request.get('email')
        adviser.pnumber = self.request.get('pnumber')
        adviser.department = self.request.get('department')
        adviser.put()
        self.redirect('/adviser/success')
    
    
class AdviserSuccessPass(webapp2.RequestHandler):
    def get(self):
        
        template = JINJA_ENVIRONMENT.get_template('AdviserSuccess.html')
        self.response.write(template.render())

class AdviserList(webapp2.RequestHandler):
    def get(self):

        adviserquery = Adviser.query().order(-Adviser.date).fetch()
        

        values = {
            'adviserquery': adviserquery,
        }


        template = JINJA_ENVIRONMENT.get_template('AdviserList.html')
        self.response.write(template.render(values))

class AdviserView(webapp2.RequestHandler):
    def get(self,adviser_id):
        
        adviserquery = Adviser.query().fetch()
        adviser_id = int(adviser_id)

        values = {
            'adviserquery': adviserquery,
            'id': adviser_id
        }

 
        template = JINJA_ENVIRONMENT.get_template('AdviserView.html')
        self.response.write(template.render(values))

class Student(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    department = ndb.StringProperty(indexed=False)
    firstname = ndb.StringProperty(indexed=False)
    lastname = ndb.StringProperty(indexed=False)
    s_num = ndb.StringProperty(indexed=False)
    emailadd = ndb.StringProperty(indexed=False)
    remarks = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class StudentNew(webapp2.RequestHandler):
    def get(self):
        
        template = JINJA_ENVIRONMENT.get_template('StudentNew.html')
        self.response.write(template.render())

    def post(self):
        student = Student()
        student.department = self.request.get('department')
        student.firstname = self.request.get('firstname')
        student.lastname = self.request.get('lastname')
        student.s_num = self.request.get('s_num')
        student.emailadd = self.request.get('emailadd')
        student.remarks = self.request.get('remarks')
        student.put()
        self.redirect('/student/success')
    
    
class StudentSuccessPass(webapp2.RequestHandler):
    def get(self):
        
        template = JINJA_ENVIRONMENT.get_template('StudentSuccess.html')
        self.response.write(template.render())

class StudentList(webapp2.RequestHandler):
    def get(self):

        studentquery = Student.query().order(-Adviser.date).fetch()
        

        values = {
            'studentquery': studentquery,
        }


        template = JINJA_ENVIRONMENT.get_template('StudentList.html')
        self.response.write(template.render(values))

class StudentView(webapp2.RequestHandler):
    def get(self,student_id):
        
        studentquery = Student.query().fetch()
        student_id = int(student_id)

        values = {
            'studentquery': studentquery,
            'id': student_id
        }

 
        template = JINJA_ENVIRONMENT.get_template('StudentView.html')
        self.response.write(template.render(values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/sign1', Guestbook1),
    ('/sign2', Guestbook2),
    ('/module-1/1', MemberOnePage),
    ('/module-1/2', MemberTwoPage),
    ('/thesis/new', ThesisNew),
    ('/thesis/success', SuccessPass),
    ('/thesis/list', ThesisList),
    ('/thesis/view/(\d+)', ThesisView),
    ('/adviser/new', AdviserNew),
    ('/adviser/success', AdviserSuccessPass),
    ('/adviser/list', AdviserList),
    ('/adviser/view/(\d+)', AdviserView),
    ('/student/new', StudentNew),
    ('/student/success', StudentSuccessPass),
    ('/student/list', StudentList),
    ('/student/view/(\d+)', StudentView),
], debug=True)
