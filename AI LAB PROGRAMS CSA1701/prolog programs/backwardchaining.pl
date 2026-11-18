
fact(rainy).
fact(cold).

wet_ground :-
    fact(rainy).

wear_jacket :-
    fact(cold).

carry_umbrella :-
    wet_ground.

backward_chaining(Goal) :-
    call(Goal).
