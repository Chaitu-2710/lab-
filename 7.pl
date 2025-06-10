% Define capacities
capacity(5, 3).

% Goal is 4 liters in Jug1
goal((4, _)).

% Valid state transitions
move((X, Y), (5, Y)) :- capacity(5, _), X < 5.            % Fill Jug1
move((X, Y), (X, 3)) :- capacity(_, 3), Y < 3.            % Fill Jug2
move((X, Y), (0, Y)) :- X > 0.                            % Empty Jug1
move((X, Y), (X, 0)) :- Y > 0.                            % Empty Jug2

% Pour Jug1 → Jug2
move((X, Y), (NX, NY)) :-
    capacity(_, MaxY),
    X > 0, Y < MaxY,
    Pour is min(X, MaxY - Y),
    NX is X - Pour,
    NY is Y + Pour.

% Pour Jug2 → Jug1
move((X, Y), (NX, NY)) :-
    capacity(MaxX, _),
    Y > 0, X < MaxX,
    Pour is min(Y, MaxX - X),
    NX is X + Pour,
    NY is Y - Pour.

% Solve the problem
water_jug(X, Y, Goal, Solution) :-
    path((X, Y), Goal, [(X, Y)], RevPath),
    reverse(RevPath, Solution).

% Find path recursively
path(State, _, Path, Path) :-
    goal(State).

path(State, Goal, Visited, Path) :-
    move(State, Next),
    \+ member(Next, Visited),
    path(Next, Goal, [Next|Visited], Path).


    ?- water_jug(0, 0, 4, Solution).
Solution = [(5, 0), (2, 3), (2, 0), (0, 2), (5, 2), (4, 3), (4, 0)].

