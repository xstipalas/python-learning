def find_best_game(games):
    ev_dict = {}
    
    for game in games:
        ev = sum(px * x for px, x in game.outcomes)
        ev_dict[ev] = game.name
        
    return ev_dict[max(ev_dict)]