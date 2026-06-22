import random
import time

with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    leaked_passwords = set(line.strip() for line in f)