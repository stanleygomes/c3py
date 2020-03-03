from project import app


class Test(app.db.Model):
  __tablename__ = 'tests'
  id = app.db.Column(app.db.Integer, primary_key=True)
  name = app.db.Column(app.db.String(80), nullable=False)
  sku = app.db.Column(app.db.String(120), nullable=False, unique=True)
