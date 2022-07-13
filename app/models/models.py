from datetime import datetime
from sqlalchemy import desc

from app import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(200))
    category = db.Column(db.String(80))
    date = db.Column(db.DateTime, default=datetime.now)
    host = db.Column(db.String(80))
    views = db.Column(db.Integer, default=0)

    def increment_view(self):
        self.views += 1
        db.session.commit()

        return self

    @staticmethod
    def get_top_three():
        entries = News.query.order_by(desc(News.views)).limit(3).all()
        return entries


