
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

h(a, 7).
h(b, 6).
h(c, 4).
h(d, 5).
h(e, 3).
h(f, 2).
h(g, 0).

best_first(Start, Goal) :-
    search([Start], Goal).

search([Goal|_], Goal) :-
    write('Goal Found: '),
    write(Goal).

search([Current|Rest], Goal) :-
    findall(H-Next,
        (edge(Current, Next), h(Next, H)),
        Children),
    keysort(Children, Sorted),
    pairs_values(Sorted, Nodes),
    append(Nodes, Rest, NewOpen),
    search(NewOpen, Goal).
