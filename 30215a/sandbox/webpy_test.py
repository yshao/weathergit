__author__ = 'Ping'

db = DAL('sqlite://storage.sqlite')
db.define_table('contact',
   Field('name'),
   Field('phone'))