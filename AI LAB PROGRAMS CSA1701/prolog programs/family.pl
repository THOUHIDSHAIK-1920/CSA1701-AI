
father(ramesh, shaik).
father(ramesh, dinesh).
father(kumar, ramesh).

mother(lakshmi, shaik).
mother(lakshmi, dinesh).
mother(sita, ramesh).

parent(X, Y) :-
    father(X, Y).

parent(X, Y) :-
    mother(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
