
person(shaik, 2005, 10, 15).
person(dinesh, 2005, 5, 20).
person(prashant, 2004, 8, 12).
person(rahul, 2005, 3, 25).

find_dob(Name, Year, Month, Day) :-
    person(Name, Year, Month, Day).
