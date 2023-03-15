import time

def before_all(context):
    context.start_time = time.time()

def after_all(context):
    end_time = time.time()
    duration = end_time - context.start_time
    print(f"Test run took {duration:.2f} seconds")