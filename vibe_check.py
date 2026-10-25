import random
import time

print('Hello! Dharani')  # your original line, still here 😎


def slow_print(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def loading(msg="Scanning your vibe"):
    print(msg, end="", flush=True)
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")


def meter(value, size=20):
    filled = round(value / 100 * size)
    return "█" * filled + "░" * (size - filled)


AURAS = {
    "Neon Purple": "mysterious, a little unhinged, always cooking 🔮",
    "Sunset Orange": "warm, chaotic good, group chat MVP 🌅",
    "Ice Blue": "calm, cold-blooded, zero stress 🧊",
    "Toxic Green": "gremlin energy, unmatched 🐸",
    "Hot Pink": "main character, no cap 💖",
    "Midnight Black": "silent but deadly, villain arc loading 🖤",
}

TITLES = [
    "Certified Lone Wolf", "Sigma in Training", "Unpaid Therapist of the Group",
    "Professional Overthinker", "Chaos Coordinator", "Bug Slayer",
    "Midnight Snack Philosopher", "NPC Who Gained Self-Awareness",
]

PROPHECIES = [
    "Someone will text you 'we need to talk'... it's about pizza. 🍕",
    "You will find money in an old hoodie this week. 💸",
    "Your next idea will go viral (in your own head). 🧠",
    "A random song will hit you SO hard at 2am. 🎧",
    "You'll win an argument you didn't even know you were in. 🏆",
    "Plot twist: you're the main character. Always were. 🎬",
]

DOORS = {
    "1": ("🚪 Door 1: Mystery Pizza", "You got a legendary slice. +50 aura."),
    "2": ("🚪 Door 2: Wi-Fi Wizard", "Your internet will never lag again. +100 speed."),
    "3": ("🚪 Door 3: Time Skip", "Monday got deleted from your calendar. Respect."),
}


def main():
    print("\n" + "=" * 44)
    print("   ✨ VIBE CHECK 3000 ✨  (no cap detector)")
    print("=" * 44 + "\n")

    name = input("What should I call you, bestie? ").strip() or "Mystery Human"
    food = input("Fav food (be honest): ").strip() or "air"

    while True:
        mood = input("Mood today, 1-10: ").strip()
        if mood.isdigit() and 1 <= int(mood) <= 10:
            mood = int(mood)
            break
        print("Bro. A number from 1 to 10. 💀")

    door = ""
    while door not in DOORS:
        door = input("Pick a door (1, 2 or 3): ").strip()
        if door not in DOORS:
            print("That door doesn't exist. Try again.")

    print()
    loading()

    # surprise output, a bit of randomness plus a bit of "you" in it
    rng = random.Random(f"{name.lower()}{food.lower()}{mood}{door}")
    aura, aura_desc = rng.choice(list(AURAS.items()))
    title = rng.choice(TITLES)
    rizz = rng.randint(40, 100)
    chaos = min(100, mood * 10 + rng.randint(-10, 15))
    iq_of_snacks = rng.randint(1, 99)
    prophecy = random.choice(PROPHECIES)  # truly random every run
    door_name, door_reward = DOORS[door]

    print("┌" + "─" * 42 + "┐")
    slow_print(f"  🎴 PLAYER CARD: {name.upper()}", 0.02)
    print("└" + "─" * 42 + "┘")
    print(f"  Title : {title}")
    print(f"  Aura  : {aura} - {aura_desc}")
    print(f"  Rizz  : {meter(rizz)} {rizz}%")
    print(f"  Chaos : {meter(chaos)} {chaos}%")
    print(f"  Snack IQ ({food}): {iq_of_snacks}/99")
    print()
    print(f"  {door_name}")
    print(f"  → {door_reward}")
    print()
    slow_print(f"  🔮 Prophecy: {prophecy}", 0.03)
    print()

    if rizz >= 90:
        print("  👑 RARE DROP: LEGENDARY RIZZ UNLOCKED. Touch grass anyway.")
    elif chaos >= 90:
        print("  🌪️ RARE DROP: Chaos Gremlin Badge. Nobody is safe.")
    else:
        print("  ✅ Vibe check passed. You're good.")

    print()
    again = input("Run it back? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        print(f"\nGG, {name}. Go build something cool. 🚀")


if __name__ == "__main__":
    main()
