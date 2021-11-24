import logging
from sqlalchemy import text

FULL_FETCH = """
SELECT
	e.employee_id,
	e.first_name,
	e.last_name,
	e.email,
	e.contact_number,
	e.designation,
	e.gender,
	d.dep_name,
	n.care_specialization,
	e.dob,
	e.hiredate,
	e.salary,
	n.shift
FROM
	employee e,
	nurse n,
	department d
WHERE
	e.employee_id = n.employee_id
AND e.department_id = d.department_id
"""

STD_FETCH = """
SELECT
	e.employee_id,
	e.first_name,
	e.last_name,
	e.email,
	e.contact_number,
	e.designation,
	e.gender,
	d.dep_name,
	n.care_specialization
FROM
	employee e,
	nurse n,
	department d
WHERE
	e.employee_id = n.employee_id
AND e.department_id = d.department_id
"""

queryMap = {
    'busy': " AND e.employee_id IN (SELECT e.employee_id FROM employee e NATURAL JOIN nurse n, admission a WHERE a.employee_id = e.employee_id AND '2021-02-25 01:01:07 PM' BETWEEN a.time_from AND a.time_to)",
    'first_name': " AND e.first_name LIKE '%%{}%%'",
    'email': " AND e.email LIKE '%%{}%%'",
    'dep_name': " AND d.dep_name LIKE '%%{}%%'",
    'specialization': " AND n.care_specialization LIKE '%%{}%%'",
    'sort': " ORDER BY e.employee_id"
}

def fetch(args):
    query = FULL_FETCH if 'sensitive' in args else STD_FETCH
    print(str(args))
    query += queryMap['busy'] if 'busy' in args else ""
    query += queryMap['first_name'].format(args['first_name']) if 'first_name' in args else ""
    query += queryMap['email'].format(args['email']) if 'email' in args else ""
    query += queryMap['dep_name'].format(args['dep_name']) if 'dep_name' in args else ""
    query += queryMap['specialization'].format(args['specialization']) if 'specialization' in args else ""
    query += queryMap['sort'] if 'sort' in args else ""
    print(str(query))
    return query