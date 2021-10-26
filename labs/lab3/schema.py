type Query{
	get_student(student_id : ID) : student
    get_class(class_id : Int) : classes
}

type Mutation{
    create_student(name : String) : [student]

    create_class(course_name : String): [classes]

    update_stu_class(
        class_id: Int!
        student_id: ID!
    ): classes
}


type student{
    student_id : ID!
    name : String
}

type classes{
    class_id : Int!
    course_name : String
    students : [student]
}