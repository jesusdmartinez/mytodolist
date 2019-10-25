from . import db


class Mytasks(db.Model):
    """Data model for mytasks"""

    __tablename__ = 'mytasks'
    id = db.Column(db.Integer,
                   primary_key=True)
    task_name = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    due_date = db.Column(db.DateTime,
                         index=False,
                         unique=False,
                         nullable=False)

    @staticmethod
    def from_dict(dict):
        return Mytasks(task_name=dict['task_name'], due_date=dict['due_date'])

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'task_name': self.task_name,
           'due_date': self.due_date
       }


class Book(db.Model):
    """Data model for books"""

    __tablename__ = 'books'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)


    @staticmethod
    def from_dict(dict):
        return Book(name=dict['name'])

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'name': self.name,
       }