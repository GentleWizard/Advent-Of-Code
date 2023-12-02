import re

with open("cubes.txt", "r") as f:
	games = [line for line in f.readlines()]
POSSIBLE_CUBES = {"red": 12, "green": 13, "blue": 14}


def create_game_dict(game):
	game_dict = {}
	game_dict["Game_ID"] = int(re.search(r"\d+", game.split(":")[0]).group())
	for pick in game.split(":")[1].split(";"):
		for cube in pick.split(","):
			if "Cubes" not in game_dict:
				game_dict["Cubes"] = {"red": 0, "blue": 0, "green": 0}
			if re.search(r"red|blue|green", cube):
				score = re.search(r"\d+", cube).group()
				color = re.search(r"red|blue|green", cube).group()
				game_dict["Cubes"][color] = max(game_dict["Cubes"][color], int(score))
	return game_dict


possible_game_ids = []
possible_game = []
for game in games:
	game_dict = create_game_dict(game)

	if all(game_dict["Cubes"][color] <= POSSIBLE_CUBES[color] for color in POSSIBLE_CUBES):
		possible_game_ids.append(game_dict["Game_ID"])
		possible_game.append(game_dict)

print(sum(possible_game_ids))
# print(possible_game)
