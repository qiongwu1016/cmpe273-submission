type Query{
	get_student(student_id : ID) : student
    get_class(class_id : Int) : classes
}

type Mutation{
    create_student(student_id : ID!,
    first_name : String,
    last_name : String,
    course_name : String) : [student]

    create_class(class_id: Int!,
    course_name : String,
    student_id : Int): [classes]

    update_stu_class(
        class_id: Int!
        student_id: ID!
    ): classes
}


type student{
    student_id : ID!
    first_name : String
    last_name : String
    course_name : String
}

type classes{
    class_id : Int!
    course_name : String
    students : [student]
}