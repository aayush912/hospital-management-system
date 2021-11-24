CREATE_EMPLOYEE = """
    INSERT INTO employee
    VALUES (
        {employee_id},
        '{first_name}',
        '{last_name}',
        '{email}',
        {contact_number},
        '{dob}',
        '{hire_date}',
        '{gender}',
        {salary},
        '{on_site}',
        '{designation}',
        {department_id})
"""
CREATE_DOCTOR = """
    INSERT INTO doctor
    VALUES (
        {employee_id},
        '{license_number}',
        '{doc_type}',
        '{specialization}'
    )
"""
CREATE_NURSE = """
    INSERT INTO nurse
    VALUES (
        {employee_id},
        '{shift}',
        '{care_specialization}'
    )
"""
CREATE_UNIT_ASSOC = """
    INSERT INTO admission
    VALUES (
        {patient_id},
        {unit_id},
        '{time_from}',
        '{time_to}',
        {employee_id}
    )
"""
GET_UNITS = """
    SELECT * FROM unit
"""
GET_DEPTS = """
    SELECT * FROM department
"""
GET_MAX_EMP_ID = """
    SELECT MAX(employee_id) FROM employee
"""

def create_doctor(eid , args):
    query = [CREATE_EMPLOYEE, CREATE_DOCTOR]
    query[0] = query[0].format(employee_id = str(int(eid) + 1), first_name = args['first_name'], last_name = args['last_name'], email = args['email'], contact_number = args['contact_number'], dob = args['dob'], hire_date = args['hire_date'], gender = args['gender'], salary = args['salary'], on_site = 'true' if 'on_site' in args else 'false', designation = args['designation'], department_id = args['department_id'])
    query[1] = query[1].format(employee_id = str(int(eid) + 1), license_number = args['license_number'], doc_type = args['doc_type'], specialization = args['specialization'])
    return query

def create_nurse(eid , args):
    query = [CREATE_EMPLOYEE, CREATE_NURSE]
    query[0] = query[0].format(employee_id = str(int(eid) + 1), first_name = args['first_name'], last_name = args['last_name'], email = args['email'], contact_number = args['contact_number'], dob = args['dob'], hire_date = args['hire_date'], gender = args['gender'], salary = args['salary'], on_site = 'true' if 'on_site' in args else 'false', designation = args['designation'], department_id = args['department_id'])
    query[1] = query[1].format(employee_id = str(int(eid) + 1), shift = args['shift'], care_specialization = args['care_specialization'])
    return query

def create_assoc(args):
    query = CREATE_UNIT_ASSOC
    query = query.format(patient_id = args['patient_id'], unit_id = args['unit_id'], time_from = args['time_from'], time_to = args['time_to'], employee_id = args['employee_id'])
    return query    