from flask import Blueprint, jsonify, request, abort
import project.api.test.test_bo as test_bo

test_v1_api = Blueprint('test_v1_api', 'test_v1_api', url_prefix='/api/v1/test')

@test_v1_api.route('/', methods=['POST'])
def insert_test():

  if not request.is_json:
    raise Exception("Esperado JSON")

  test = request.get_json()

  # TODO Validar
  # pass

  id = test_bo.insert_test(test)
  return jsonify(id=id)


@test_v1_api.route('/<id>', methods=['GET'])
def get_by_id(id):
    # TODO validar ha ID
    test = test_bo.find_by_id(id)
    if test is None:
        return abort(404)
    return jsonify(test.serialize)

