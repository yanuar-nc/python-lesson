from flask import request
from flask_restful import Resource
from app import response
from app.model import Article

class Index(Resource):
	def get(self):
		
		articles = Article.query.all()
		
		data_all = []

		for article in articles:
			result = {
				'id': article.id,
				'title': article.title,
				'content': article.content
			}
			data_all.append(result)

		return data_all

class Detail(Resource):
	def get(self, article_id):

		article = Article.query.filter_by(id=article_id).first()

		if not article:
			return False, 404

		result = {
			'id': article.id,
			'title': article.title,
			'content': article.content
		}
		return response(result)

