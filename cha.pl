% Define the distance between two cities (both directions)
distance(a, b, 10).
distance(b, a, 10).
distance(b, c, 15).
distance(c, b, 15).
distance(c, d, 20).
distance(d, c, 20).
distance(d, a, 25).
distance(a, d, 25).
distance(a, c, 30).
distance(c, a, 30).
distance(b, d, 35).
distance(d, b, 35).

% Base case for tsp/2 (only one city, no distance)
tsp([_], 0). % Use _ for the singleton variable

% Recursive case for tsp/2 (list of cities)
tsp([City1, City2 | Rest], Distance) :-
    distance(City1, City2, D),
    tsp([City2 | Rest], D2),
    Distance is D + D2.

% Find the shortest route by calculating distances for all permutations
find_shortest_route(Cities, ShortestRoute, Distance) :-
    permutation(Cities, Route),
    tsp(Route, Distance), % Calculate the distance for this permutation
    \+ (permutation(Cities, AnotherRoute), tsp(AnotherRoute, D), D < Distance), % Check if this is the shortest
    ShortestRoute = Route.

% Main predicate to find the shortest route
solve_tsp(Cities, ShortestRoute, Distance) :-
    find_shortest_route(Cities, ShortestRoute, Distance).
