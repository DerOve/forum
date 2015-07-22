from google.appengine.ext import ndb

class User(ndb.Model):
    first_name = ndb.StringProperty(default=None)
    last_name = ndb.StringProperty(default=None)
    email = ndb.StringProperty()
    receive_updates = ndb.BooleanProperty(default=True)
    is_admin = ndb.BooleanProperty(default=False)


    @classmethod
    def create(cls, email, is_admin):
        topic = cls(email = email, is_admin = is_admin)
        topic.put()
        return topic