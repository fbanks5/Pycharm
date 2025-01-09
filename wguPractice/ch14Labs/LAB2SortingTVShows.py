# Read the input file name
input_filename = input().strip()

# Initialize the dictionary to store seasons as keys and TV shows as values
seasons_dict = {}

# Read and process the input file
with open(input_filename, 'r') as file:
    lines = file.readlines()

    # Loop through lines in pairs: season and TV show
    for i in range(0, len(lines), 2):
        seasons = int(lines[i].strip())  # First line is the season count
        tv_show = lines[i + 1].strip()  # Second line is the TV show name

        # Add the TV show to the dictionary under the appropriate season key
        if seasons not in seasons_dict:
            seasons_dict[seasons] = []
        seasons_dict[seasons].append(tv_show)

# Write to output_keys.txt sorted by keys (seasons)
with open("output_keys.txt", 'w') as file:
    for seasons in sorted(seasons_dict.keys()):
        tv_shows = "; ".join(seasons_dict[seasons])  # Join TV shows with a semicolon
        file.write(f"{seasons}: {tv_shows}\n")

# Write to output_titles.txt sorted alphabetically by TV show titles
with open("output_titles.txt", 'w') as file:
    # Extract all TV shows into a single list and sort alphabetically
    sorted_titles = sorted([tv_show for shows in seasons_dict.values() for tv_show in shows])
    for tv_show in sorted_titles:
        file.write(f"{tv_show}\n")