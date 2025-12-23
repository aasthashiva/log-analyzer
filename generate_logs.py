import random
from datetime import datetime, timedelta

start_time = datetime(2024, 12, 21, 10, 0, 0)
entries = 100000
current_time = start_time

mode = "normal"
mode_timer = 0

# Open the file ONCE, overwrite every run
with open("generated.log", "w") as f:
    for i in range(entries):
        # advance time
        current_time += timedelta(seconds=random.choice([1, 1, 2]))

        # switch modes occasionally
        if mode_timer <= 0:
            roll = random.random()
            if roll < 0.7:
                mode = "normal"
                mode_timer = random.randint(50, 120)
            elif roll < 0.9:
                mode = "degraded"
                mode_timer = random.randint(20, 40)
            else:
                mode = "failure"
                mode_timer = random.randint(5, 15)

        mode_timer -= 1

        # assign severity & latency based on mode
        if mode == "normal":
            level = "INFO"
            latency = random.randint(110, 140)
        elif mode == "degraded":
            level = random.choice(["INFO", "WARN"])
            latency = random.randint(180, 350)
        else:  # failure mode
            level = random.choice(["ERROR", "WARN"])
            latency = random.randint(700, 1300)

        # write log line
        f.write(
            f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"{level} latency={latency}\n"
        )

print("Log generation complete: generated.log created")
