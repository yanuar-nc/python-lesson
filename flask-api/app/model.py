from main import db
from flask_validator import ValidateInteger, ValidateString, ValidateEmail

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text(),nullable=False)
    post_date = db.Column(db.DateTime(),nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.title

    @classmethod
    def __declare_last__(cls):
    	ValidateString(Article.title, False, False, "Aww")