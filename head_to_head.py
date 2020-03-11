import pandas as pd


teams = ["Illinois", "Purdue", "Iowa", "Indiana", "Ohio State", "Penn State", "Minnesota", "Michigan", "Michigan State",
          "Rutgers", "Maryland", "Northwestern", "Nebraska", "Wisconsin"]
# ranks from analysis.py
ranks = [8,9,7,4,12,6,3,10,14,5,13,2,1,11]
# from tourney bracket
seeds = [4,10,5,11,7,6,12,9,2,8,3,13,14,1]
rank_df = pd.DataFrame({'team': teams,'rank' : ranks, 'seed' : seeds})

head_to_head = {}

for t in teams:
	inter_dict = {}
	for x in teams:
		if x not in [t]:
			inter_dict[x] = {'win_rate': None, 'games': None}
	head_to_head[t] = inter_dict


def add_win_rate(dict= head_to_head, home= None, away=None, rate=None, games = None):
	dict[home][away]['win_rate'] = rate
	dict[away][home]['win_rate'] = 1- rate
	dict[home][away]['games'] = games
	dict[away][home]['games'] = games

	return dict

def add_prob(dict, rank_df, home = None):
	home_rank = int(rank_df[rank_df['team'] == home]['rank'])
	for away in dict[home]:
		away_rank = int(rank_df[rank_df['team'] == away]['rank'])
		diff = home_rank - away_rank
		prob = 1/(1 + 10**(-diff*(30.464/400)))
		win_rate = dict[home][away]['win_rate']
		games = dict[home][away]['games']
		if games == 2:
			weights = [.75,.25]
		else:
			weights = [.85, .15]
		final_prob = weights[0]*prob + weights[1]*win_rate
		dict[home][away]['prob'] = final_prob
	return dict


def bracket(rank_df = rank_df, dict = head_to_head, team = None):
	seed = int(rank_df[rank_df['team'] == team]['seed'])
	first_round = [(11,14), (12,13)]
	second_round =[(8,9), (11,14,6), (5,12,13), (10,7)]
	quarters = [(1,8,9), (4,5,12,13), (2,7,10), (3,6,11,14)]
	semis = [(1,8,9,4,5,12,13), (2,7,10,3,6,11,14)]
	champs = [(1,8,9,4,5,12,13,2,7,10,3,6,11,14)]
	if seed <= 4:
		first_round = 1
		second_round = 1
	elif seed <= 10:
		first_round = 1
	if seed == 11:
		first_round_opp =





# Illinois
home = 'Illinois'
head_to_head = add_win_rate(home = home, away = 'Iowa', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Maryland', rate =0, games = 2)
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Michigan State', rate =0, games =2)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Wisconsin', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Penn State', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Ohio State', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Rutgers', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =1, games = 2)
# Maryland
home = 'Maryland'
head_to_head = add_win_rate(home = home, away = 'Iowa', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Michigan State', rate =.5, games =2)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Wisconsin', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Penn State', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Ohio State', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Rutgers', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =1, games = 1)

# M ST
home = 'Michigan State'
head_to_head = add_win_rate(home = home, away = 'Iowa', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Wisconsin', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Penn State', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Ohio State', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Rutgers', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =0, games = 1)

# Wisconsin
home = 'Wisconsin'
head_to_head = add_win_rate(home = home, away = 'Iowa', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Penn State', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Ohio State', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Rutgers', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =.5, games = 2)

# Ohio State
home = 'Ohio State'
head_to_head = add_win_rate(home = home, away = 'Iowa', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Penn State', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Rutgers', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =0, games = 2)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =1, games = 1)


# Penn State
home = 'Penn State'
head_to_head = add_win_rate(home = home, away = 'Iowa', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Rutgers', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =1, games = 1)

# Iowa
home = 'Iowa'
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =.5, games = 2)
head_to_head = add_win_rate(home = home, away = 'Rutgers', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =0, games = 2)

# Rutgers
home = 'Rutgers'
head_to_head = add_win_rate(home = home, away = 'Michigan', rate =0, games = 2)
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =1, games = 2)


# Mich
home = 'Michigan'
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Indiana', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =1, games = 2)


# Ind
home = 'Indiana'
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =1, games = 2)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Purdue', rate =0, games = 2)


# Purdue
home = 'Purdue'
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =0, games = 1)
head_to_head = add_win_rate(home = home, away = 'Minnesota', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 2)

# Minn
home = 'Minnesota'
head_to_head = add_win_rate(home = home, away = 'Nebraska', rate =1, games = 1)
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =1, games = 2)


# Nebraska
home = 'Nebraska'
head_to_head = add_win_rate(home = home, away = 'Northwestern', rate =0, games = 2)

# add probabilities

for t in teams:
	head_to_head = add_prob(dict=head_to_head, rank_df=rank_df,home =t)


