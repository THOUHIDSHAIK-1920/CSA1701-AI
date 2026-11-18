
fact(rainy).
fact(cold).

rule(wet_ground) :-
    fact(rainy).

rule(wear_jacket) :-
    fact(cold).

rule(carry_umbrella) :-
    rule(wet_ground).

forward_chaining(X) :-
    rule(X).
