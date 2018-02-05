# List of routes

from app.resources.article import Index as ArticleIndex, Detail as ArticleDetail
from main import api

api.add_resource(ArticleIndex, '/articles')
api.add_resource(ArticleDetail, '/articles/<int:article_id>')
