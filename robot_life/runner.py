import time

def basic_run_field(
    field,
    handler,
    population_period=0.1,
    maximal_history_capacity=1_000_000,
    timer=time.time,
    sleeper=time.sleep,
):
    field_history = [field]
    previous_time = timer()
    while True:
        handler(field)

        field = field.populate()
        if field in field_history:
            break

        field_history.append(field)
        if len(field_history) > maximal_history_capacity:
            field_history.pop(0)

        current_time = timer()
        elapsed_time = current_time - previous_time
        if elapsed_time < population_period:
            sleeper(population_period - elapsed_time)

        previous_time = current_time
