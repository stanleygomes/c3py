from project import app
from .test_model import Test

def validate_test(test):
  if test is None:
    raise Exception('Cadê o produto?')


def insert_new_test(new_test, db=app.db, can_commit=True):
  db.session.add(new_test)
  if can_commit:
    db.session.commit()


def insert_test(test):
  validate_test(test)

  new_test = Test.from_dict(test)

  new_test = Test(name=test['name'], sku=test['sku'])
  insert_new_test(new_test)

  return new_test.id

def find_by_id(id):
  id = int(id)
  return Test.query.get(id)


