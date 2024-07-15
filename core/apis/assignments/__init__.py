from .student import student_assignments_resources
from .teacher import teacher_assignments_resources
# core/apis/assignments/init_.py
from flask import Blueprint

assignments_bp = Blueprint('assignments', _name_)

from core.apis.assignments import principal, student, teacher

assignments_bp.add_url_rule('/principal/assignments', view_func=principal.get_principal_assignments, methods=['GET'])
assignments_bp.add_url_rule('/principal/teachers', view_func=principal.get_principal_teachers, methods=['GET'])
assignments_bp.add_url_rule('/principal/assignments/grade', view_func=principal.grade_assignment_principal, methods=['POST'])
assignments_bp.add_url_rule('/student/assignments', view_func=student.get_student_assignments, methods=['GET'])
assignments_bp.add_url_rule('/student/assignments', view_func=student.create_assignment, methods=['POST'])
assignments_bp.add_url_rule('/student/assignments', view_func=student.edit_assignment, methods=['POST'])
assignments_bp.add_url_rule('/student/assignments/submit', view_func=student.submit_assignment, methods=['POST'])
assignments_bp.add_url_rule('/teacher/assignments', view_func=teacher.get_teacher_assignments, methods=['GET'])
assignments_bp.add_url_rule('/teacher/assignments/grade', view_func=teacher.grade_assignment, methods=['POST'])
