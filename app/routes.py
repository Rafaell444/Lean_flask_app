from flask import request
from flask_restful import Resource, marshal_with, fields
from app import api, db
from app.models.models import News


class topThree(fields.Raw):
    def format(self, value):
        return f"Top 3 popular articles: 1) {value[0].title} 2) {value[1].title} 3) {value[2].title}"


newsFields = {
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "category": fields.String,
    "date": fields.DateTime,
    "host": fields.String,
    "views": fields.Integer
}


class All_News(Resource):
    @marshal_with(newsFields)
    def get(self):
        news = News.query.all()

        return news

    @marshal_with(newsFields)
    def post(self):
        data = request.json

        new = News(title=data.get('title'),
                   description=data.get('description'),
                   category=data.get('category'),
                   host=data.get('host'))

        db.session.add(new)
        db.session.commit()

        news = News.query.all()
        return news


class New(Resource):
    @marshal_with(newsFields)
    def get(self, pk):
        new = News.query.get(pk)

        new.increment_view()

        new.top_three = News.get_top_three()
        newsFields['top_three'] = topThree()

        return new

    @marshal_with(newsFields)
    def put(self, pk):
        data = request.json
        new = News.query.get(pk)

        new.title = data.get("title")
        new.description = data.get("description")
        new.category = data.get("category")
        new.host = data.get("host")
        db.session.commit()

        return new

    @marshal_with(newsFields)
    def delete(self, pk):
        new = News.query.get(pk)
        db.session.delete(new)
        db.session.commit()
        news = News.query.all()
        return news


api.add_resource(All_News, '/')
api.add_resource(New, '/<int:pk>')
