
can_reach(monkey, floor).
can_reach(box, floor).
can_reach(monkey, box).
can_reach(monkey, banana).

monkey_banana :-
    can_reach(monkey, floor),
    can_reach(box, floor),
    can_reach(monkey, box),
    can_reach(monkey, banana),
    write('Monkey gets the banana!').
