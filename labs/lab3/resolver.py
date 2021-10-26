import json
from pprint import pprint

global_student_id = 2000000
global_class_id = 500

all_students = [
    {
        "student_id": 1000007,
        "name": "Jasper"
    },
    {
        "student_id": 1000008,
        "name": "Jujube"
    },
    {
        "student_id": 1000009,
        "name": "Qiong"
    }
]

all_classes = [
    {
        "class_id": 330,
        "course_name": "English",
        "students": [
        {
            "student_id": 1000007,
            "name": "Jasper"
        }
        ]
    },
    {
        "class_id": 340,
        "course_name": "Math",
        "students": [
        {
            "student_id": 1000008,
            "name": "Jujube"
        },
        {
            "student_id": 1000009,
            "name": "Qiong"
        }

        ]
    }
]


def get_student(_, info, student_id):
    studs = [stu for stu in all_students if stu["student_id"] == int(student_id)]    
    return studs[0]

def get_class(_, info, class_id):
    global all_classes
    found = False
    for c in all_classes:
        if c['class_id'] == class_id:
            found = True
            break   
    if found is True:
        return c




def create_student(_, info, name):
    global all_student, global_student_id
    all_students.append({'student_id' : global_student_id, 'name': name, 'course_name':[]})
    global_student_id = global_student_id + 1
    return all_students

def create_class(_, info, course_name):
    global all_classes, all_student, global_class_id  
    all_classes.append({"class_id":global_class_id, "course_name":course_name, "students": []})
    global_class_id = global_class_id + 1
    return all_classes

def update_stu_class(_, info, class_id, student_id):
    global all_classes, all_students
    class_found = False
    stu_found = False
    for stu in all_students:
        if stu['student_id'] == int(student_id):
            stu_found = True
            break
    if stu_found is True:
        print(type(stu))
    else:
        print("student not found")
    if stu_found is True:
        for c in all_classes:
            if c['class_id'] == int(class_id):
                class_found = True
                c['students'].append(stu)
                break
        if class_found is True:
            return c
    
