
pattern(hello, greeting).
pattern(hi, greeting).
pattern(bye, farewell).
pattern(goodbye, farewell).
pattern(thanks, gratitude).

match_pattern(Input, Output) :-
    pattern(Input, Output).
