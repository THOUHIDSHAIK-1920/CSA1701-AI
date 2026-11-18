
can_fly(parrot).
can_fly(eagle).
can_fly(pigeon).
can_fly(sparrow).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

bird_status(Bird, can_fly) :-
    can_fly(Bird).

bird_status(Bird, cannot_fly) :-
    cannot_fly(Bird).
