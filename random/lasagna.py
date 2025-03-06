EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_time

def preparation_time_in_minutes(number_of_layers):
    mins_per_layer = 2
    prep_time = number_of_layers * mins_per_layer
    return prep_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    elapsed_time = preparation_time_in_minutes(number_of_layers) + (EXPECTED_BAKE_TIME - bake_time_remaining(elapsed_bake_time)) 
    return elapsed_time
