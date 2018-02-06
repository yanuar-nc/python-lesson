from main import app, db
from flask import request
from flask_restful import Resource
from app import response
from app.model import Article
from app.validators import ArticleForm

class Index(Resource):
	def get(self):
		
		page = request.args.get('page', 1, type=int)

		articles = Article.query.paginate(page, app.config['POSTS_PER_PAGE'], False)
		
		data_all = []

		for article in articles.items:
			result = {
				'id': article.id,
				'title': article.title,
				'content': article.content
			}
			data_all.append(result)

		result = {
			'pagination': {
				'current': articles.page,
				'total_pages': articles.pages,
				'total_items': articles.total,
			},
			'articles': data_all
		};
		return response(result)

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


class Insert(Resource):
	def post(self):

		data = request.form;

		form = ArticleForm(data)
		if form.validate():
			new_article = Article(
				title=data['title'], 
				content=data['content'], 
				post_date=data['post_date']
			)
			
			db.session.add(new_article)
			db.session.commit()

			return response({'id': new_article.id})
		else:
			return response(form.get_error_messages(), 400)


