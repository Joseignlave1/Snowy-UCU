from flask import Blueprint, jsonify, request
from controllers.student_controller import (
    getAllStudentsEndpoint,
    getStudentById,
    addStudentEndpoint,
    modifyStudent,
    deleteStudent
)

student_bp = Blueprint('student_bp', __name__)

@student_bp.route("/students/all", methods=['GET'])
def getAllStudents():
    students = getAllStudentsEndpoint()
    return jsonify(students)

@student_bp.route("/students/<int:student_id>", methods=['GET'])
def getStudentByIdRoute(student_id):
    student = getStudentById(student_id)
    if student:
        return jsonify(student)
    else:
        return jsonify({'message': 'Student not found'}), 404

@student_bp.route("/students", methods=['POST'])
def addStudent():
    data = request.json
    student_id = data.get('id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birth_date = data.get('birth_date')
    contact_phone = data.get('contact_phone')
    email_address = data.get('email_address')
    result = addStudentEndpoint(student_id, first_name, last_name, birth_date, contact_phone, email_address)
    return jsonify(result), 201

@student_bp.route("/students/<int:student_id>", methods=['PUT'])
def modifyStudentRoute(student_id):
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birth_date = data.get('birth_date')
    contact_phone = data.get('contact_phone')
    email_address = data.get('email_address')
    result = modifyStudent(student_id, first_name, last_name, birth_date, contact_phone, email_address)
    return jsonify(result)

@student_bp.route("/students/<int:student_id>", methods=['DELETE'])
def deleteStudentRoute(student_id):
    result = deleteStudent(student_id)
    return jsonify(result)