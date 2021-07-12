import time

def basic_run_field(
    field,
    handler,
    population_period=0.1,
    timer=time.time,
    sleeper=time.sleep,
):
    previous_time = timer()
    while True:
        handler(field)

        field = field.populate()

        current_time = timer()
        elapsed_time = current_time - previous_time
        if elapsed_time < population_period:
            sleeper(population_period - elapsed_time)

        previous_time = current_time
