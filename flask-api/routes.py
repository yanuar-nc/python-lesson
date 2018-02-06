# List of routes

from app.resources.article import Index as ArticleIndex, \
								  Detail as ArticleDetail, \
								  Insert as ArticleInsert
from main import api

api.add_resource(ArticleIndex, '/article/all')
api.add_resource(ArticleInsert, '/article/insert')
api.add_resource(ArticleDetail, '/article/<int:article_id>')
