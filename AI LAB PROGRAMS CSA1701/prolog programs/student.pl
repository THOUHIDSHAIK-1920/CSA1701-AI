
student(shaik, ramesh, 'ITA0609').
student(dinesh, kumar, 'CSA1701').
student(prashant, raj, 'CSA5802').
student(rahul, anil, 'ITA0609').

student_details(Student, Teacher, Subject) :-
    student(Student, Teacher, Subject).
