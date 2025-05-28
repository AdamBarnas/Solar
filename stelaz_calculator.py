# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

available_profiles = []

for i in range(4):
    available_profiles.append(4000)
for i in range(17):
    available_profiles.append(2000)
for i in range(1):
    available_profiles.append(750)
for i in range(1):
    available_profiles.append(1600)
for i in range(3):
    available_profiles.append(450)

available_profiles.sort()



# print("Available profiles:")
# for i in available_prfiles:
#     print(i)
all_profiles = np.array(available_profiles)
available_profiles = np.array(available_profiles)
print("Available profiles sum:", available_profiles.sum())

# %%
profiles = []

for i in range(2):
    profiles.append(3516)
for i in range(2):
    profiles.append(2740)
for i in range(4):
    profiles.append(1149+5)
for i in range(4):
    profiles.append(1220)
for i in range(4):
    profiles.append(1066)
for i in range(2):
    profiles.append(1040)
for i in range(4):
    profiles.append(530)
for i in range(2):
    profiles.append(760)
for i in range(4):
    profiles.append(560)
for i in range(2):
    profiles.append(740)
for i in range(2):
    profiles.append(525)
profiles.append(665)


profiles.sort()
# print("Profile:")
# for i in profile:
#     print(i)
profiles.reverse()
profiles = np.array(profiles)


print(profiles.sum(), "\n")
print(len(profiles), "\n")

# %%
dictionary = {}

for profile in profiles:
    ok = False
    best = None
    best_index = None
    for i in range(len(available_profiles)):
        if profile <= available_profiles[i]:
            if best is None or available_profiles[i] < best:
                best = available_profiles[i]
                best_index = i
            ok = True
            break
    if not ok:
        print(f"Profile {profile} cannot be made with available profiles")
        break
    else:
        if best_index not in dictionary:
            dictionary[best_index] = []
        dictionary[best_index].append(int(profile))
        available_profiles[best_index] -= profile
        print(f"Profile {profile} allocated with {available_profiles[best_index] + profile} -> {available_profiles[best_index]}    \tindex {best_index}")

# print("Available profiles after allocation:")
# for i in available_profiles:
#     print(i)
print("Available profiles sum after allocation:", available_profiles.sum())

print("Dictionary:")
for key in dictionary:
    print(f"{all_profiles[key]}: {dictionary[key]}")

fig, ax = plt.subplots(figsize=(10, 6))

y = 0
for key in dictionary:
    profile_length = all_profiles[key]
    pieces = dictionary[key]
    x = 0
    # Draw the main profile as a light rectangle
    ax.add_patch(
        patches.Rectangle((0, y), profile_length, 1, edgecolor='black', facecolor='lightgray', lw=1)
    )
    # Draw each allocated piece as a colored rectangle
    for piece in pieces:
        ax.add_patch(
            patches.Rectangle((x, y), piece, 1, edgecolor='black', facecolor='tab:blue', lw=2)
        )
        x += piece
    y += 2  # Space between profiles

ax.set_xlim(0, max(all_profiles))
ax.set_ylim(0, y)
ax.set_xlabel('Length')
ax.set_ylabel('Profile')
ax.set_title('Profile Allocations')
plt.tight_layout()
plt.show()