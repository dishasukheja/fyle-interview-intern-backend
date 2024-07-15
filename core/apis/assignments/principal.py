from flask import request, jsonify
from core.libs.responses import success_response, error_response
from core.models import Assignment, Teacher
from core.libs.decorators import principal_required

@principal_required
def get_principal_assignments():
    """
    List all submitted and graded assignments
    """
    try:
        assignments = Assignment.query.filter(
            Assignment.state.in_(['SUBMITTED', 'GRADED'])
        ).all()

        return success_response(data=[assignment.to_dict() for assignment in assignments])
    except Exception as e:
        return error_response(message=str(e))

@principal_required
def get_principal_teachers():
    """
    List all the teachers
    """
    try:
        teachers = Teacher.query.all()
        return success_response(data=[teacher.to_dict() for teacher in teachers])
    except Exception as e:
        return error_response(message=str(e))

@principal_required
def grade_assignment_principal():
    """
    Grade or re-grade an assignment
    """
    try:
        data = request.get_json()
        assignment_id = data.get('id')
        grade = data.get('grade')

        if not assignment_id or not grade:
            return error_response(message="Missing id or grade")

        assignment = Assignment.query.get(assignment_id)
        if not assignment:
            return error_response(message="Assignment not found")

        # Intentional bug: The principal should be able to re-grade assignments regardless of the teacher
        # Remove this check to fix the bug:
        # if assignment.teacher_id != teacher_id:
        #     return error_response(message="You are not authorized to grade this assignment")

        assignment.grade = grade
        assignment.state = 'GRADED'
        assignment.save()

        return success_response(data=assignment.to_dict())
    except Exception as e:
        return error_response(message=str(e))