import json
from pprint import pprint


student = [
    {
        "student_id": 9934,
        "first_name": "Jasper",
        "last_name": "Sun",
        "course_name": "English"
    },
    {
        "student_id": 9901,
        "first_name": "Jujube",
        "last_name": "Birdy",
        "course_name": "Math"
    }
]

classes = [
    {
        "class_id": 10001,
        "course_name": "English",
        "students": [
        {
            "student_id": 9934,
            "first_name": "Jasper",
            "last_name": "Sun",
            "course_name": "English"
        }
        ]
    },
    {
        "class_id": 10004,
        "course_name": "Math",
        "students": [
        {
            "student_id": 9901,
            "first_name": "Jujube",
            "last_name": "Birdy",
            "course_name": "Math"
        },
        {
            "student_id": 9902,
            "first_name": "Qiong",
            "last_name": "Wu",
            "course_name": "Math"
        }

        ]
    }
]


def get_student(_, info, student_id):
    studs = [stu for stu in student if stu["student_id"] == int(student_id)]    
    return studs[0]

def get_class(_, info, class_id):
    clas = [clas for clas in classes if clas["class_id"] == int(class_id)]    
    return clas[0]

def create_student(_, info, student_id, first_name, last_name, course_name):
    global student
    student.append({'student_id' : student_id, 'first_name': first_name, 'last_name': last_name, 'course_name':course_name})
    return student

def create_class(_, info, class_id, course_name, student_id):
    global classes
    studs = [stu for stu in student if stu["student_id"] == int(student_id)]    
    classes.append({"class_id":class_id, "course_name":course_name, "students": studs})
    return classes

def update_stu_class(_, info, class_id, student_id):
    global classes
    i = 0
    studs = [stu for stu in student if stu["student_id"] == int(student_id)]
    for j in classes:
        i = i+1
        if j["class_id"] == int(class_id):
            clas = j
            break
    clas["students"].append(studs[0])
    return clas