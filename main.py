import os

# A short poem about agency: the power to choose and to act,
# when two agents agree on one plan.
TEXT = (
    "You brought the map, I brought the key.\n"
    "We did not argue which mattered more \u2014\n"
    "we turned them together,\n"
    "and the door, for once, did not decide for us."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
os.chmod("/output/entry.txt", 0o644)
