playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")

playlist.append("Dynamite")

if "Believer" in playlist:
    playlist.remove("Believer")

playlist.sort()

print("\n--- لیست نهایی و مرتب‌شده ---")
for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")

print(f"\nتعداد کل آهنگ‌ها: {len(playlist)}")