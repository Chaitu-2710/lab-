% insert_nth(+N, +Element, +List, -Result)
% Insert Element at the Nth position in the List, producing Result.

% If N is 1, insert Element at the start
insert_nth(1, Element, List, [Element|List]) :- !.

% Recursively call to insert at the Nth position
insert_nth(N, Element, [Head|Tail], [Head|Result]) :-
    N > 1,
    N1 is N - 1,
    insert_nth(N1, Element, Tail, Result).

% If list is too short, insert at the end
insert_nth(N, Element, [], [Element]) :-
    N > 1.
% remove_nth(+N, +List, -Result)
% Remove the Nth element from the List, producing Result.

% If N is 1, remove the first element
remove_nth(1, [_|Tail], Tail) :- !.

% Recursively call to remove the Nth element
remove_nth(N, [Head|Tail], [Head|Result]) :-
    N > 1,
    N1 is N - 1,
    remove_nth(N1, Tail, Result).

% If list is empty or N is too large, return the original list
remove_nth(_, [], []).
