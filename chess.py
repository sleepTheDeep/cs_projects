from random import randint
from time import sleep


#cards
skeletons = ["skeletons", 1, 0, 0, 0, 0, 1.1, 2]
fire_spirit = ["fire spirit", 1, 0, 0, 1, 4, 0, 3]
electro_spirit = ["electro spirit", 0, 0, 0, 1, 4, 0, 3]
ice_spirit = ["ice spirit", 1, 0, 0, 1, 4, 0, 3]
goblins = ["goblins", 2, 0, 0, 0, 0, 1.1, 3]
spear_goblins = ["spear goblins", 2, 0, 0, 1, 3, 1.7, 3]
bomber = ["bomber", 2, 0, 0, 0, 3, 1.8, 1]
bats = ["bats", 2, 0, 0, 1, 1, 1.3, 3]
zap = ["zap", 2, 0, 1, 1, 4, 0, 4]
snowball = ["snowball", 2, 0, 1, 1, 4, 0, 4]
berserker = ["berserker", 2, 0, 0, 0, 0, 0.6, 2]
knight = ["knight", 3, 0, 0, 0, 1, 1.2, 1]
archers = ["archers", 3, 0, 0, 1, 4, 0.9, 1]
minions = ["minions", 3, 0, 0, 1, 0, 1.1, 2]
arrows = ["arrows", 3, 0, 1, 1, 4, 0, 4]
cannon = ["cannon", 3, 0, 2, 0, 3, 1, 4]
goblin_gang = ["goblin gang", 3, 0, 0, 1, 3, 1.4, 3]
skeleton_barrel = ["skeleton barrel", 3, 0, 0, 0, 0, 1.1, 2]
firecracker = ["fire cracker", 3, 0, 0, 1, 3, 3, 2]
royal_delivery = ["royal delivery", 3, 0, 1, 1, 2, 1.3, 1]
skeleton_dragons = ["skeleton dragons", 4, 0, 0, 1, 3, 1.9, 2]
mortar = ["mortar", 4, 0, 2, 0, 3, 5, 4]
tesla = ["tesla", 4, 0, 2, 1, 3, 1.1, 4]
barbarians = ["barbarians", 5, 0, 0, 0, 0, 1.3, 1]
minion_horde = ["minion horde", 5, 0, 0, 1, 0, 1.1, 2]
rascals = ["rascals", 5, 0, 0, 1, 0, 1.25, 1]
royal_giant = ["royal giant", 6, 0, 0, 2, 3, 1.7, 0]
elite_barbarians = ["elite barbarians", 6, 0, 0, 0, 1, 1.4, 2]
royal_recruits = ["royal recruits", 7, 0, 0, 0, 2, 1.3, 1]
heal_spirit = ["heal spirit", 1, 1, 0, 1, 4, 0, 3]
ice_golem = ["ice golem", 2, 1, 0, 2, 0, 2.5, 0]
suspicious_bush = ["suspicious bush", 2, 1, 0, 0, 0, 1.4, 1]
tombstone = ["tombstone", 3, 1, 2, 0, 0, 4, 2]
mega_minion = ["mega minion", 3, 1, 0, 1, 2, 1.5, 1]
dart_goblin = ["dart goblin", 3, 1, 0, 1, 3, 0.8, 3]
earthquake = ["earthquake", 3, 1, 1, 0, 4, 0, 4]
elixir_golem = ["elixir golem", 3, 1, 0, 2, 0, 1.1, 0]
musketeer = ["musketeer", 4, 1, 0, 1, 3, 1, 1]
mini_pekka = ["mini pekka", 4, 1, 0, 0, 0, 1.6, 2]
goblin_hut = ["goblin hut", 4, 1, 2, 1, 3, 1.9, 4]
goblin_cage = ["goblin cage", 4, 1, 2, 0, 0, 0, 4]
fireball = ["fireball", 4, 1, 1, 1, 4, 0, 4]
valkyrie = ["valkyrie", 4, 1, 0, 0, 1, 1.5, 1]
battle_ram = ["battle ram", 4, 1, 0, 2, 0, 1.3, 1]
bomb_tower = ["bomb tower", 4, 1, 2, 0, 3, 1.8, 4]
hog_rider = ["hog rider", 4, 1, 0, 2, 0, 1.6, 3]
flying_machine = ["flying machine", 4, 1, 0, 1, 3, 1.1, 2]
battle_healer = ["battle healer", 4, 1, 0, 0, 2, 1.5, 1]
zappies = ["zappies", 4, 1, 0, 1, 3, 2.1, 1]
furnace = ["furnace", 4, 1, 0, 1, 3, 1.8, 1]
goblin_demolisher = ["goblin demolisher", 4, 1, 0, 0, 3, 1.2, 1]
giant = ["heal spirit", 5, 1, 0, 1, 1, 1.5, 1]
wizard = ["giant", 5, 1, 0, 1, 3, 1.4, 1]
inferno_tower = ["inferno tower", 5, 1, 2, 1, 3, 0.4, 4]
royal_hogs = ["royal hogs", 5, 1, 0, 2, 0, 1.2, 0]
rocket = ["rocket", 6, 1, 1, 1, 4, 0, 4]
barbarian_hut = ["barbarian hut", 6, 1, 2, 0, 0, 15, 4]
elixir_pump = ["elixir pump", 6, 1, 2, 0, 0, 12, 4]
three_musketeers = ["three musketeers", 9, 1, 0, 1, 3, 1, 1]
mirror = ["mirror", "?", 2, 1, 1, 0, 0, 4]
barbarian_barrel = ["barbarian barrel", 2, 2, 1, 0, 0, 1.3, 1]
wall_breakers = ["wall breakers", 2, 2, 0, 2, 0, 0, 3]
rage = ["rage", 2, 2, 1, 1, 4, 0, 4]
goblin_curse = ["goblin curse", 2, 2, 1, 1, 4, 6, 4]
skeleton_army = ["skeleton army", 3, 2, 0, 0, 0, 1.1, 2]
guards = ["guards", 3, 2, 0, 0, 0, 1, 2]
goblin_barrel = ["goblin barrel", 3, 2, 1, 0, 0, 1.1, 3]
vines = ["vines", 3, 2, 1, 1, 4, 2, 4]
tornado = ["tornado", 3, 2, 1, 1, 4, 1, 4]
clone = ["clone", 3, 2, 1, 1, 4, 0, 4]
void = ["void", 3, 2, 1, 1, 4, 4, 4]
baby_dragon = ["baby dragon", 4, 2, 0, 1, 3, 1.5, 2]
dark_prince = ["dark prince", 4, 2, 0, 0, 1, 1.3, 1]
freeze = ["freeze", 4, 2, 1, 1, 4, 4, 4]
rune_giant = ["rune giant", 4, 2, 0, 2, 1, 1.5, 1]
poison = ["poison", 4, 2, 1, 1, 4, 8, 4]
hunter = ["hunter", 4, 2, 0, 1, 3, 2.2, 1]
goblin_drill = ["goblin drill", 4, 2, 0, 0, 0, 3, 4]
witch = ["witch", 5, 2, 0, 1, 3, 1.1, 1]
balloon = ["balloon", 5, 2, 0, 2, 0, 2, 1]
prince = ["prince", 5, 2, 0, 0, 2, 1.4, 1]
electro_dragon = ["electro dragon", 5, 2, 0, 1, 3, 2.1, 1]
bowler = ["bowler", 5, 2, 0, 0, 3, 2.5, 0]
executioner = ["executioner", 5, 2, 0, 1, 3, 2.4, 1]
cannon_cart = ["cannon cart", 5, 2, 0, 0, 3, 0.9, 1]
giant_skeleton = ["giant skeleton", 6, 2, 0, 0, 0, 1.4, 1]
lightning = ["lightning", 6, 2, 1, 1, 4, 0, 4]
goblin_giant = ["goblin giant", 6, 2, 0, 2, 1, 1.5, 1]
xbow = ["xbow", 6, 2, 2, 0, 3, 0.3, 4]
pekka = ["pekka", 7, 2, 0, 0, 1, 1.8, 0]
electro_giant = ["electro giant", 7, 2, 0, 2, 1, 2.1, 0]
golem = ["golem", 8, 2, 0, 2, 0, 2.5, 0]
log = ["log", 2, 3, 1, 0, 4, 0, 4]
royal_ghost = ["royal ghost", 3, 3, 0, 0, 1, 1.8, 2]
princess = ["princess", 3, 3, 0, 1, 3, 3, 1]
miner = ["miner", 3, 3, 0, 0, 1, 1.3, 2]
ice_wizard = ["ice_wizard", 3, 3, 0, 1, 3, 1.7, 1]
bandit = ["bandit", 3, 3, 0, 0, 0, 1, 2]
fisherman = ["fisherman", 3, 3, 0, 0, 1, 1.3, 1]
inferno_dragon = ["inferno dragon", 4, 3, 0, 1, 3, 0.4, 1]
electro_wizard = ["electro wizard", 4, 3, 0, 1, 3, 1.8, 2]
phoenix = ["phoenix", 4, 3, 0, 1, 2, 1, 1]
magic_archer = ["magic archer", 4, 3, 0, 1, 3, 1.1, 1]
lumberjack = ["lumberjack", 4, 3, 0, 0, 0, 0.8, 3]
night_witch = ["night witch", 4, 3, 0, 0, 2, 1.3, 1]
mother_witch = ["mother witch", 4, 3, 0, 1, 3, 1, 1]
graveyard = ["graveyard", 5, 3, 1, 0, 0, 1.1, 4]
ram_rider = ["ram rider", 5, 3, 0, 2, 0, 1.8, 1]
goblin_machine = ["goblin machine", 5, 3, 0, 0, 1, 1.2, 1]
sparky = ["sparky", 6, 3, 0, 0, 3, 4, 0]
spirit_empress = ["spirit empress", 6, 3, 0, 1, 3, 1.4, 1]
mega_knight = ["mega knight", 7, 3, 0, 0, 1, 1.7, 1]
lava_hound = ["lava hound", 7, 3, 0, 2, 3, 1.3, 0]
little_prince = ["little prince", 3, 4, 0, 1, 3, 0.8, 1]
golden_knight = ["golden knight", 4, 4, 0, 0, 1, 0.9, 1]
mighty_miner = ["mighty miner", 4, 4, 0, 0, 2, 0.4, 1]
skeleton_king = ["skeleton king", 4, 4, 0, 0, 1, 1.6, 1]
monk = ["monk", 5, 4, 0, 0, 1, 0.8, 1]
goblinstein = ["goblinstein", 5, 4, 0, 1, 3, 1.8, 1]
archer_queen = ["archer queen", 5, 4, 0, 1, 3, 1.2, 1]
boss_bandit = ["boss bandit", 6, 4, 0, 0, 0, 1.2, 2]


#================================================================================ Classic mode lists ================================================================================
card_names = [skeletons[0], fire_spirit[0], electro_spirit[0], ice_spirit[0], goblins[0], spear_goblins[0], bomber[0], bats[0], zap[0], snowball[0], berserker[0],
             knight[0], archers[0], minions[0], arrows[0], cannon[0], goblin_gang[0], skeleton_barrel[0], firecracker[0], royal_delivery[0], skeleton_dragons[0],
             mortar[0], tesla[0], barbarians[0], minion_horde[0], rascals[0], royal_giant[0], elite_barbarians[0], royal_recruits[0], heal_spirit[0], ice_golem[0],
             suspicious_bush[0], tombstone[0], mega_minion[0], dart_goblin[0], earthquake[0], elixir_golem[0], musketeer[0], mini_pekka[0], goblin_hut[0], goblin_cage[0],
             fireball[0], valkyrie[0], battle_ram[0], bomb_tower[0], hog_rider[0], flying_machine[0], battle_healer[0], zappies[0], furnace[0], goblin_demolisher[0],
             giant[0], wizard[0], inferno_tower[0], royal_hogs[0], rocket[0], barbarian_hut[0], elixir_pump[0], three_musketeers[0], mirror[0], barbarian_barrel[0],
             wall_breakers[0], rage[0], goblin_curse[0], guards[0], goblin_barrel[0], vines[0], tornado[0], clone[0], void[0], baby_dragon[0], skeleton_army[0], dark_prince[0],
             freeze[0], poison[0], hunter[0], goblin_drill[0], witch[0], balloon[0], prince[0], electro_dragon[0], bowler[0], executioner[0], cannon_cart[0], giant_skeleton[0],
             lightning[0], goblin_giant[0], xbow[0], pekka[0], electro_giant[0], golem[0], log[0], princess[0], miner[0], ice_wizard[0], bandit[0], fisherman[0], royal_ghost[0],
             inferno_dragon[0], electro_wizard[0], phoenix[0], magic_archer[0], lumberjack[0], night_witch[0], mother_witch[0], graveyard[0], ram_rider[0], goblin_machine[0],
             sparky[0], spirit_empress[0], mega_knight[0], lava_hound[0], little_prince[0], golden_knight[0], mighty_miner[0], skeleton_king[0], monk[0], goblinstein[0],
             boss_bandit[0]]


card_elixirs = [skeletons[1], fire_spirit[1], electro_spirit[1], ice_spirit[1], goblins[1], spear_goblins[1], bomber[1], bats[1], zap[1], snowball[1], berserker[1],
              knight[1], archers[1], minions[1], arrows[1], cannon[1], goblin_gang[1], skeleton_barrel[1], firecracker[1], royal_delivery[1], skeleton_dragons[1],
              mortar[1], tesla[1], barbarians[1], minion_horde[1], rascals[1], royal_giant[1], elite_barbarians[1], royal_recruits[1], heal_spirit[1], ice_golem[1],
              suspicious_bush[1], tombstone[1], mega_minion[1], dart_goblin[1], earthquake[1], elixir_golem[1], musketeer[1], mini_pekka[1], goblin_hut[1], goblin_cage[1],
              fireball[1], valkyrie[1], battle_ram[1], bomb_tower[1], hog_rider[1], flying_machine[1], battle_healer[1], zappies[1], furnace[1], goblin_demolisher[1],
              giant[1], wizard[1], inferno_tower[1], royal_hogs[1], rocket[1], barbarian_hut[1], elixir_pump[1], three_musketeers[1], mirror[1], barbarian_barrel[1],
              wall_breakers[1], rage[1], goblin_curse[1], guards[1], goblin_barrel[1], vines[1], tornado[1], clone[1], void[1], baby_dragon[1], skeleton_army[1], dark_prince[1],
              freeze[1], poison[1], hunter[1], goblin_drill[1], witch[1], balloon[1], prince[1], electro_dragon[1], bowler[1], executioner[1], cannon_cart[1], giant_skeleton[1],
              lightning[1], goblin_giant[1], xbow[1], pekka[1], electro_giant[1], golem[1], log[1], princess[1], miner[1], ice_wizard[1], bandit[1], fisherman[1], royal_ghost[1],
              inferno_dragon[1], electro_wizard[1], phoenix[1], magic_archer[1], lumberjack[1], night_witch[1], mother_witch[1], graveyard[1], ram_rider[1], goblin_machine[1],
              sparky[1], spirit_empress[1], mega_knight[1], lava_hound[1], little_prince[1], golden_knight[1], mighty_miner[1], skeleton_king[1], monk[1], goblinstein[1],
              boss_bandit[1]]


card_rarities = [skeletons[2], fire_spirit[2], electro_spirit[2], ice_spirit[2], goblins[2], spear_goblins[2], bomber[2], bats[2], zap[2], snowball[2], berserker[2],
              knight[2], archers[2], minions[2], arrows[2], cannon[2], goblin_gang[2], skeleton_barrel[2], firecracker[2], royal_delivery[2], skeleton_dragons[2],
              mortar[2], tesla[2], barbarians[2], minion_horde[2], rascals[2], royal_giant[2], elite_barbarians[2], royal_recruits[2], heal_spirit[2], ice_golem[2],
              suspicious_bush[2], tombstone[2], mega_minion[2], dart_goblin[2], earthquake[2], elixir_golem[2], musketeer[2], mini_pekka[2], goblin_hut[2], goblin_cage[2],
              fireball[2], valkyrie[2], battle_ram[2], bomb_tower[2], hog_rider[2], flying_machine[2], battle_healer[2], zappies[2], furnace[2], goblin_demolisher[2],
              giant[2], wizard[2], inferno_tower[2], royal_hogs[2], rocket[2], barbarian_hut[2], elixir_pump[2], three_musketeers[2], mirror[2], barbarian_barrel[2],
              wall_breakers[2], rage[2], goblin_curse[2], guards[2], goblin_barrel[2], vines[2], tornado[2], clone[2], void[2], baby_dragon[2], skeleton_army[2], dark_prince[2],
              freeze[2], poison[2], hunter[2], goblin_drill[2], witch[2], balloon[2], prince[2], electro_dragon[2], bowler[2], executioner[2], cannon_cart[2], giant_skeleton[2],
              lightning[2], goblin_giant[2], xbow[2], pekka[2], electro_giant[2], golem[2], log[2], princess[2], miner[2], ice_wizard[2], bandit[2], fisherman[2], royal_ghost[2],
              inferno_dragon[2], electro_wizard[2], phoenix[2], magic_archer[2], lumberjack[2], night_witch[2], mother_witch[2], graveyard[2], ram_rider[2], goblin_machine[2],
              sparky[2], spirit_empress[2], mega_knight[2], lava_hound[2], little_prince[2], golden_knight[2], mighty_miner[2], skeleton_king[2], monk[2], goblinstein[2],
              boss_bandit[2]]


card_types = [skeletons[3], fire_spirit[3], electro_spirit[3], ice_spirit[3], goblins[3], spear_goblins[3], bomber[3], bats[3], zap[3], snowball[3], berserker[3],
             knight[3], archers[3], minions[3], arrows[3], cannon[3], goblin_gang[3], skeleton_barrel[3], firecracker[3], royal_delivery[3], skeleton_dragons[3],
             mortar[3], tesla[3], barbarians[3], minion_horde[3], rascals[3], royal_giant[3], elite_barbarians[3], royal_recruits[3], heal_spirit[3], ice_golem[3],
             suspicious_bush[3], tombstone[3], mega_minion[3], dart_goblin[3], earthquake[3], elixir_golem[3], musketeer[3], mini_pekka[3], goblin_hut[3], goblin_cage[3],
             fireball[3], valkyrie[3], battle_ram[3], bomb_tower[3], hog_rider[3], flying_machine[3], battle_healer[3], zappies[3], furnace[3], goblin_demolisher[3],
             giant[3], wizard[3], inferno_tower[3], royal_hogs[3], rocket[3], barbarian_hut[3], elixir_pump[3], three_musketeers[3], mirror[3], barbarian_barrel[3],
             wall_breakers[3], rage[3], goblin_curse[3], guards[3], goblin_barrel[3], vines[3], tornado[3], clone[3], void[3], baby_dragon[3], skeleton_army[3], dark_prince[3],
             freeze[3], poison[3], hunter[3], goblin_drill[3], witch[3], balloon[3], prince[3], electro_dragon[3], bowler[3], executioner[3], cannon_cart[3], giant_skeleton[3],
             lightning[3], goblin_giant[3], xbow[3], pekka[3], electro_giant[3], golem[3], log[3], princess[3], miner[3], ice_wizard[3], bandit[3], fisherman[3], royal_ghost[3],
             inferno_dragon[3], electro_wizard[3], phoenix[3], magic_archer[3], lumberjack[3], night_witch[3], mother_witch[3], graveyard[3], ram_rider[3], goblin_machine[3],
             sparky[3], spirit_empress[3], mega_knight[3], lava_hound[3], little_prince[3], golden_knight[3], mighty_miner[3], skeleton_king[3], monk[3], goblinstein[3],
             boss_bandit[3]]


card_targets = [skeletons[4], fire_spirit[4], electro_spirit[4], ice_spirit[4], goblins[4], spear_goblins[4], bomber[4], bats[4], zap[4], snowball[4], berserker[4],
              knight[4], archers[4], minions[4], arrows[4], cannon[4], goblin_gang[4], skeleton_barrel[4], firecracker[4], royal_delivery[4], skeleton_dragons[4],
              mortar[4], tesla[4], barbarians[4], minion_horde[4], rascals[4], royal_giant[4], elite_barbarians[4], royal_recruits[4], heal_spirit[4], ice_golem[4],
              suspicious_bush[4], tombstone[4], mega_minion[4], dart_goblin[4], earthquake[4], elixir_golem[4], musketeer[4], mini_pekka[4], goblin_hut[4], goblin_cage[4],
              fireball[4], valkyrie[4], battle_ram[4], bomb_tower[4], hog_rider[4], flying_machine[4], battle_healer[4], zappies[4], furnace[4], goblin_demolisher[4],
              giant[4], wizard[4], inferno_tower[4], royal_hogs[4], rocket[4], barbarian_hut[4], elixir_pump[4], three_musketeers[4], mirror[4], barbarian_barrel[4],
              wall_breakers[4], rage[4], goblin_curse[4], guards[4], goblin_barrel[4], vines[4], tornado[4], clone[4], void[4], baby_dragon[4], skeleton_army[4], dark_prince[4],
              freeze[4], poison[4], hunter[4], goblin_drill[4], witch[4], balloon[4], prince[4], electro_dragon[4], bowler[4], executioner[4], cannon_cart[4], giant_skeleton[4],
              lightning[4], goblin_giant[4], xbow[4], pekka[4], electro_giant[4], golem[4], log[4], princess[4], miner[4], ice_wizard[4], bandit[4], fisherman[4], royal_ghost[4],
              inferno_dragon[4], electro_wizard[4], phoenix[4], magic_archer[4], lumberjack[4], night_witch[4], mother_witch[4], graveyard[4], ram_rider[4], goblin_machine[4],
              sparky[4], spirit_empress[4], mega_knight[4], lava_hound[4], little_prince[4], golden_knight[4], mighty_miner[4], skeleton_king[4], monk[4], goblinstein[4],
              boss_bandit[4]]


card_ranges = [skeletons[5], fire_spirit[5], electro_spirit[5], ice_spirit[5], goblins[5], spear_goblins[5], bomber[5], bats[5], zap[5], snowball[5], berserker[5],
              knight[5], archers[5], minions[5], arrows[5], cannon[5], goblin_gang[5], skeleton_barrel[5], firecracker[5], royal_delivery[5], skeleton_dragons[5],
              mortar[5], tesla[5], barbarians[5], minion_horde[5], rascals[5], royal_giant[5], elite_barbarians[5], royal_recruits[5], heal_spirit[5], ice_golem[5],
              suspicious_bush[5], tombstone[5], mega_minion[5], dart_goblin[5], earthquake[5], elixir_golem[5], musketeer[5], mini_pekka[5], goblin_hut[5], goblin_cage[5],
              fireball[5], valkyrie[5], battle_ram[5], bomb_tower[5], hog_rider[5], flying_machine[5], battle_healer[5], zappies[5], furnace[5], goblin_demolisher[5],
              giant[5], wizard[5], inferno_tower[5], royal_hogs[5], rocket[5], barbarian_hut[5], elixir_pump[5], three_musketeers[5], mirror[5], barbarian_barrel[5],
              wall_breakers[5], rage[5], goblin_curse[5], guards[5], goblin_barrel[5], vines[5], tornado[5], clone[5], void[5], baby_dragon[5], skeleton_army[5], dark_prince[5],
              freeze[5], poison[5], hunter[5], goblin_drill[5], witch[5], balloon[5], prince[5], electro_dragon[5], bowler[5], executioner[5], cannon_cart[5], giant_skeleton[5],
              lightning[5], goblin_giant[5], xbow[5], pekka[5], electro_giant[5], golem[5], log[5], princess[5], miner[5], ice_wizard[5], bandit[5], fisherman[5], royal_ghost[5],
              inferno_dragon[5], electro_wizard[5], phoenix[5], magic_archer[5], lumberjack[5], night_witch[5], mother_witch[5], graveyard[5], ram_rider[5], goblin_machine[5],
              sparky[5], spirit_empress[5], mega_knight[5], lava_hound[5], little_prince[5], golden_knight[5], mighty_miner[5], skeleton_king[5], monk[5], goblinstein[5],
              boss_bandit[5]]


card_hitspeeds = [skeletons[6], fire_spirit[6], electro_spirit[6], ice_spirit[6], goblins[6], spear_goblins[6], bomber[6], bats[6], zap[6], snowball[6], berserker[6],
              knight[6], archers[6], minions[6], arrows[6], cannon[6], goblin_gang[6], skeleton_barrel[6], firecracker[6], royal_delivery[6], skeleton_dragons[6],
              mortar[6], tesla[6], barbarians[6], minion_horde[6], rascals[6], royal_giant[6], elite_barbarians[6], royal_recruits[6], heal_spirit[6], ice_golem[6],
              suspicious_bush[6], tombstone[6], mega_minion[6], dart_goblin[6], earthquake[6], elixir_golem[6], musketeer[6], mini_pekka[6], goblin_hut[6], goblin_cage[6],
              fireball[6], valkyrie[6], battle_ram[6], bomb_tower[6], hog_rider[6], flying_machine[6], battle_healer[6], zappies[6], furnace[6], goblin_demolisher[6],
              giant[6], wizard[6], inferno_tower[6], royal_hogs[6], rocket[6], barbarian_hut[6], elixir_pump[6], three_musketeers[6], mirror[6], barbarian_barrel[6],
              wall_breakers[6], rage[6], goblin_curse[6], guards[6], goblin_barrel[6], vines[6], tornado[6], clone[6], void[6], baby_dragon[6], skeleton_army[6], dark_prince[6],
              freeze[6], poison[6], hunter[6], goblin_drill[6], witch[6], balloon[6], prince[6], electro_dragon[6], bowler[6], executioner[6], cannon_cart[6], giant_skeleton[6],
              lightning[6], goblin_giant[6], xbow[6], pekka[6], electro_giant[6], golem[6], log[6], princess[6], miner[6], ice_wizard[6], bandit[6], fisherman[6], royal_ghost[6],
              inferno_dragon[6], electro_wizard[6], phoenix[6], magic_archer[6], lumberjack[6], night_witch[6], mother_witch[6], graveyard[6], ram_rider[6], goblin_machine[6],
              sparky[6], spirit_empress[6], mega_knight[6], lava_hound[6], little_prince[6], golden_knight[6], mighty_miner[6], skeleton_king[6], monk[6], goblinstein[6],
              boss_bandit[6]]


card_speeds = [skeletons[7], fire_spirit[7], electro_spirit[7], ice_spirit[7], goblins[7], spear_goblins[7], bomber[7], bats[7], zap[7], snowball[7], berserker[7],
              knight[7], archers[7], minions[7], arrows[7], cannon[7], goblin_gang[7], skeleton_barrel[7], firecracker[7], royal_delivery[7], skeleton_dragons[7],
              mortar[7], tesla[7], barbarians[7], minion_horde[7], rascals[7], royal_giant[7], elite_barbarians[7], royal_recruits[7], heal_spirit[7], ice_golem[7],
              suspicious_bush[7], tombstone[7], mega_minion[7], dart_goblin[7], earthquake[7], elixir_golem[7], musketeer[7], mini_pekka[7], goblin_hut[7], goblin_cage[7],
              fireball[7], valkyrie[7], battle_ram[7], bomb_tower[7], hog_rider[7], flying_machine[7], battle_healer[7], zappies[7], furnace[7], goblin_demolisher[7],
              giant[7], wizard[7], inferno_tower[7], royal_hogs[7], rocket[7], barbarian_hut[7], elixir_pump[7], three_musketeers[7], mirror[7], barbarian_barrel[7],
              wall_breakers[7], rage[7], goblin_curse[7], guards[7], goblin_barrel[7], vines[7], tornado[7], clone[7], void[7], baby_dragon[7], skeleton_army[7], dark_prince[7],
              freeze[7], poison[7], hunter[7], goblin_drill[7], witch[7], balloon[7], prince[7], electro_dragon[7], bowler[7], executioner[7], cannon_cart[7], giant_skeleton[7],
              lightning[7], goblin_giant[7], xbow[7], pekka[7], electro_giant[7], golem[7], log[7], princess[7], miner[7], ice_wizard[7], bandit[7], fisherman[7], royal_ghost[7],
              inferno_dragon[7], electro_wizard[7], phoenix[7], magic_archer[7], lumberjack[7], night_witch[7], mother_witch[7], graveyard[7], ram_rider[7], goblin_machine[7],
              sparky[7], spirit_empress[7], mega_knight[7], lava_hound[7], little_prince[7], golden_knight[7], mighty_miner[7], skeleton_king[7], monk[7], goblinstein[7],
              boss_bandit[7]]






#================================================================================ Emoji mode lists ================================================================================
skeletons1 = ["3️⃣", "️⚔️", "🪦", "💀", "skeletons"]
fire_spirit1 = ["1️⃣", "🪨", "✨", "🔥", "fire spirit"]
electro_spirit1 = ["1️⃣", "🪨", "⚡", "✨", "electro spirit"]
ice_spirit1 = ["1️⃣", "🧊", "❄️", "✨", "ice spirit"]
goblins1 = ["4️⃣", "🤢", "⚔️", "😈", "goblins"]
spear_goblins1 = ["3️⃣", "🏹", "🤢", "😈", "spear goblins"]
bomber1 = ["1️⃣", "💣", "✝️", "💀", "bomber"]
bats1 = ["5️⃣", "🧛", "🪽", "😈", "bats"]
zap1 = ["🧪", "💨", "⚡", "◼️", "zap"]
snowball1 = ["⚪", "🌨️", "❄️", "🧊", "snowball"]
berserker1 = ["1️⃣", "🧒", "⚔️", "💢", "berserker"]
knight1 = ["1️⃣", "⚔️", "👑", "🪖", "knight"]
archers1 = ["2️⃣", "🏹", "👧", "🎯", "archers"]
minions1 = ["3️⃣", "😡", "🧤", "🪽", "minions"]
arrows1 = ["🏹", "⬆️", "🎯", "💘", "arrows"]
cannon1 = ["🏗️", "🥫", "⚫", "🎯", "cannon"]
goblin_gang1 = ["6️⃣", "⚔️", "🏹", "🤢", "goblin gang"]
skeleton_barrel1 = ["🍯", "🎈", "✝️", "💀", "skeleton barrel"]
firecracker1 = ["1️⃣", "👧", "🏹", "🎆", "fire cracker"]
royal_delivery1 = ["🛡️", "🥫", "🏰", "👨", "royal delivery"]
skeleton_dragons1 = ["2️⃣", "🪽", "🔥", "💀", "skeleton dragons"]
mortar1 = ["🏹", "🏗️", "⚫", "4️⃣", "mortar"]
tesla1 = ["🏗️", "4️⃣", "⚡", "🔌", "tesla"]
barbarians1 = ["5️⃣", "⚔️", "👨", "👨", "barbarians"]
minion_horde1 = ["6️⃣", "🧤", "😡", "🪽", "minion horde"]
rascals1 = ["3️⃣", "👨‍👧‍👧", "🏹", "⚔️", "rascals"]
royal_giant1 = ["👨", "⚫", "👑", "🏰", "royal giant"]
elite_barbarians1 = ["👨", "👨", "⚔️", "💢", "elite barbarians"]
royal_recruits1 = ["🛡️", "👑", "👨", "⚔️", "royal recruits"]
heal_spirit1 = ["🪨", "💨", "✨", "👨‍⚕️", "heal spirit"]
ice_golem1 = ["🪨", "✨", "🧊", "👣", "ice golem"]
suspicious_bush1 = ["🥬", "🪨", "🥷", "🤢", "suspicious bush"]
tombstone1 = ["🪦", "🦴", "😵", "💀", "tombstone"]
mega_minion1 = ["🛡️", "🧤", "😡", "🪽", "mega minion"]
dart_goblin1 = ["🏹", "😡", "🤢", "😷", "dart goblin"]
earthquake1 = ["🧪", "🪨", "🫨", "😵", "earthquake"]
elixir_golem1 = ["😡", "🧤", "👨‍👩‍👧‍👦", "💜", "elixir golem"]
musketeer1 = ["👧", "🔫", "💥", "⚫", "musketeer"]
mini_pekka1 = ["🤖", "⚔️", "🥞", "💥", "mini pekka"]
goblin_hut1 = ["🏹", "🤢", "🏡", "💨", "goblin hut"]
goblin_cage1 = ["💪", "🤢", "🏡", "🚧", "goblin cage"]
fireball1 = ["🪨", "🔥", "🧪", "✨", "fireball"]
valkyrie1 = ["👩", "🛡️", "🪓", "✨", "valkyrie"]
battle_ram1 = ["🪵", "👨", "🧔‍♂️", "⚔️", "battle ram"]
bomb_tower1 = ["🏗️", "💣", "💥", "💀", "bomb tower"]
hog_rider1 = ["🐗", "💥", "🪓", "👨", "hog rider"]
flying_machine1 = ["🪽", "👨", "🔫", "💥", "flying machine"]
battle_healer1 = ["👩", "🪽", "🧑‍⚕️", "✨", "battle healer"]
zappies1 = ["⚡", "3️⃣", "🔌", "⚙️", "zappies"]
furnace1 = ["👨", "🔥", "🪨", "⚕️", "furnace"]
goblin_demolisher1 = ["🧨", "💣", "💥", "🤢", "goblin demolisher"]
giant1 = ["👣", "💪", "🏗️", "🏰", "giant"]
wizard1 = ["🧙‍♂️", "🔥", "✨", "💥", "wizard"]
inferno_tower1 = ["🏗️", "🔥", "💥", "⚙️", "inferno tower"]
royal_hogs1 = ["🐗", "👑", "🏠", "🏰", "royal hogs"]
rocket1 = ["💨", "🔥", "🚀", "💣", "rocket"]
barbarian_hut1 = ["👨", "⚔️", "🏠", "💢", "barbarian hut"]
elixir_pump1 = ["⚙️", "🏠", "⛽", "💜", "elixir pump"]
three_musketeers1 = ["👧", "👧", "👧", "🔫", "three musketeers"]
mirror1 = ["🐑", "🐑", "🧪", "🪞", "mirror"]
barbarian_barrel1 = ["👨", "⚔️", "🥫", "💢", "barbarian barrel"]
wall_breakers1 = ["🥫", "💣", "💥", "💀", "wall breakers"]
rage1 = ["🧪", "⚡", "💢", "😈", "rage"]
goblin_curse1 = ["🧪", "🤢", "⚡", "💥", "goblin curse"]
skeleton_army1 = ["💀", "💀", "💀", "💀", "skeleton army"]
guards1 = ["🛡️", "💀", "💀", "⚔️", "guards"]
goblin_barrel1 = ["🥫", "🤢", "🤢", "⚔️", "goblin barrel"]
vines1 = ["🧪", "🌲", "⬇️", "🌲", "vines"]
tornado1 = ["☁️", "💨", "🌪️", "🧪", "tornado"]
clone1 = ["🟰", "🧪", "1️⃣", "🥛", "clone"]
void1 = ["🔥", "⚡", "🧪", "🧙", "void"]
baby_dragon1 = ["🐲", "🔥", "🔥", "👶", "baby dragon"]
dark_prince1 = ["👨", "🛡️", "🐎", "⬛", "dark prince"]
freeze1 = ["🧪", "❄️", "🥶", "🧊", "freeze"]
rune_giant1 = ["👩", "🪓", "💢", "🧡", "rune giant"]
poison1 = ["🧪", "☠️", "🧡", "4️⃣", "poison"]
hunter1 = ["👨", "🔫", "💥", "🥅", "hunter"]
goblin_drill1 = ["🏠", "🕳️", "⚔️", "🤢", "goblin drill"]
witch1 = ["🧙‍♀️", "🪦", "💀", "🏹", "witch"]
balloon1 = ["🎈", "💥", "💀", "💣", "balloon"]
prince1 = ["👨", "🛡️", "🐎", "⚔️", "prince"]
electro_dragon1 = ["🐲", "⚡", "⚡", "🔵", "electro dragon"]
bowler1 = ["👨", "🧤", "💨", "🎳", "bowler"]
executioner1 = ["🪓", "👨", "💨", "😡", "executioner"]
cannon_cart1 = ["🏠", "🚗", "🔫", "⚫", "cannon cart"]
giant_skeleton1 = ["💀", "👣", "💥", "💣", "giant skeleton"]
lightning1 = ["⚡", "🌩️", "⛈️", "🧪", "lightning"]
goblin_giant1 = ["👣", "🏹", "🏹", "🤢", "goblin giant"]
xbow1 = ["🏠", "🏹", "🎯", "🏰", "xbow"]
pekka1 = ["🤖", "⚔️", "🦋", "👣", "pekka"]
electro_giant1 = ["👨", "👣", "⚡", "⚡", "electro giant"]
golem1 = ["🪨", "👣", "👣", "✨", "golem"]
log1 = ["✨", "🪓", "🪵", "🪵", "log"]
royal_ghost1 = ["🪦", "👑", "👻", "⚔️", "royal ghost"]
princess1 = ["👑", "👸", "🏹", "🔥", "princess"]
miner1 = ["👨", "🪖", "🕳️", "😏", "miner"]
ice_wizard1 = ["🧙‍♂️", "❄️", "🥶", "🧊", "ice wizard"]
bandit1 = ["😏", "💨", "👩", "⚔️", "bandit"]
fisherman1 = ["🐟", "⚓", "👨", "🥊", "fisherman"]
inferno_dragon1 = ["🐲", "👶", "🔥", "💥", "inferno dragon"]
electro_wizard1 = ["🧙‍♂️", "⚡", "⛈️", "🌩️", "electro wizard"]
phoenix1 = ["🥚", "🔥", "🐦", "🐦‍🔥", "phoenix"]
magic_archer1 = ["👨", "✨", "🏹", "✨", "magic archer"]
lumberjack1 = ["👨", "🪓", "🪵", "🥴", "lumberjack"]
night_witch1 = ["🧙‍♀️", "🌃", "🦇", "🦇", "night witch"]
mother_witch1 = ["👵", "🧙‍♀️", "🧪", "🐗", "mother witch"]
graveyard1 = ["🕳️", "🪦", "☠️", "💀", "graveyard"]
ram_rider1 = ["👩", "🪨", "🪢", "🐏", "ram rider"]
goblin_machine1 = ["👶", "⚙️", "🚀", "💥", "goblin machine"]
sparky1 = ["⚙️", "🚗", "⚡", "💥", "sparky"]
spirit_empress1 = ["🐲", "👩", "⚔️", "✨", "spirit empress"]
mega_knight1 = ["👣", "👑", "👨", "👊", "mega knight"]
lava_hound1 = ["🐕", "🔥", "🪽", "7️⃣", "lava hound"]
little_prince1 = ["👶", "👑", "🏹", "🛡️", "little prince"]
golden_knight1 = ["🧔‍♂️", "👑", "⚔️", "🥇", "golden knight"]
mighty_miner1 = ["🕳️", "😏", "💣", "💥", "mighty miner"]
skeleton_king1 = ["👑", "🛡️", "💀", "👥", "skeleton king"]
monk1 = ["🧓", "🛡️", "🪃", "💨", "monk"]
goblinstein1 = ["🤪", "👣", "⚡", "🤢", "goblinstein"]
archer_queen1 = ["👑", "🏹", "👩", "🧥", "archer queen"]
boss_bandit1 = ["👩", "🔎", "👑", "💨", "boss bandit"]


emoji_list = [skeletons1, fire_spirit1, electro_spirit1, ice_spirit1, goblins1, spear_goblins1, bomber1, bats1, zap1, snowball1, berserker1, knight1, archers1, minions1,
             arrows1, cannon1, goblin_gang1, skeleton_barrel1, firecracker1, royal_recruits1, skeleton_dragons1, mortar1, tesla1, barbarians1, minion_horde1, rascals1,
             royal_giant1, elite_barbarians1, royal_recruits1, heal_spirit1, ice_golem1, suspicious_bush1, tombstone1, mega_minion1, dart_goblin1, earthquake1, elixir_golem1,
             musketeer1, mini_pekka1, goblin_hut1, goblin_cage1, fireball1, valkyrie1, battle_ram1, bomb_tower1, hog_rider1, flying_machine1, battle_healer1, zappies1,
             furnace1, goblin_demolisher1, giant1, wizard1, inferno_tower1, royal_hogs1, rocket1, barbarian_hut1, elixir_pump1, three_musketeers1, mirror1, barbarian_barrel1,
             wall_breakers1, rage1, goblin_curse1, guards1, goblin_barrel1, vines1, tornado1, clone1, void1, baby_dragon1, dark_prince1, freeze1, rune_giant1, poison1,
             hunter1, goblin_drill1, witch1, balloon1, prince1, electro_dragon1, bowler1, executioner1, cannon_cart1, giant_skeleton1, lightning1, goblin_giant1, xbow1,
             pekka1, electro_giant1, golem1, log1, royal_ghost1, princess1, miner1, ice_wizard1, bandit1, fisherman1, inferno_dragon1, electro_wizard1, phoenix1,
             magic_archer1, lumberjack1, night_witch1, mother_witch1, graveyard1, ram_rider1, goblin_machine1, sparky1, spirit_empress1, mega_knight1, lava_hound1,
             little_prince1, golden_knight1, mighty_miner1, monk1, goblinstein1, archer_queen1, boss_bandit1]


#================================================================================ Description mode lists ================================================================================
skeletons2 = ["skeletons", "Three", "fast,", "very", "weak", "melee", "fighters.", "Surround", "your", "enemies", "with", "this", "pile", "of", "bones!"]
fire_spirit2 = ["fire spirit", "The", "Fire", "Spirit", "is", "on", "a", "mission", "to", "give", "you", "a", "warm", "hug.", "It'd", "be", "adorable", "if", "it", "wasn't", "on", "fire."]
electro_spirit2 = ["electro spirit", "Jumps", "on", "enemies,", "dealing", "Area", "Damage", "and", "stunning", "up", "to", "9", "enemy", "Troops.", "Locked", "in", "an", "eternal", "battle", "with", "Knight", "for", "the", "best", "moustache"]
ice_spirit2 = ["ice spirit", "Spawns", "one", "lively", "little", "Ice", "Spirit", "to", "freeze", "a", "group", "of", "enemies.", "Stay", "frosty."]
goblins2 = ["goblins", "Four", "fast,", "unarmored", "melee", "attackers.", "Small,", "fast,", "green", "and", "mean!"]
spear_goblins2 = ["spear goblins", "Three", "unarmored", "ranged", "attackers.", "Who", "the", "heck", "taught", "these", "guys", "to", "throw", "spears!?", "Who", "thought", "that", "was", "a", "good", "idea?!"]
bomber2 = ["bomber", "Small,", "lightly", "protected", "skeleton", "who", "throws", "bombs.", "Deals", "area", "damage", "that", "can", "wipe", "out", "a", "swarm", "of", "enemies."]
bats2 = ["bats", "Spawns", "a", "handful", "of", "tiny", "flying", "creatures.", "Think", "of", "them", "as", "sweet,", "purple...", "balls", "of", "DESTRUCTION!"]
zap2 = ["zap", "Zaps", "enemies,", "briefly", "stunning", "them", "and", "dealing", "damage", "inside", "a", "small", "radius.", "Reduced", "damage", "to", "Crown", "Towers."]
snowball2 = ["snowball", "It's", "HUGE!", "Once", "it", "began", "rolling", "down", "Frozen", "Peak,", "there", "was", "no", "stopping", "it.", "Enemies", "hit", "are", "knocked", "back", "and", "slowed", "down.", "Reduced", "damage", "to", "Crown", "Towers."]
berserker2 = ["berserker", "It's", "surprising", "how", "often", "she", "needs", "her", "axes", "sharpened,", "but", "then", "again,", "if", "you", "liked", "hitting", "things", "as", "fast", "as", "her,", "so", "would", "you."]
knight2 = ["knight", "A", "tough", "melee", "fighter.", "The", "Barbarian's", "handsome,", "cultured", "cousin.", "Rumor", "has", "it", "that", "he", "was", "knighted", "based", "on", "the", "sheer", "awesomeness", "of", "his", "moustache", "alone."]
archers2 = ["archers", "A", "pair", "of", "lightly", "armoured", "ranged", "attackers.", "They'll", "help", "you", "take", "down", "ground", "air", "units,", "but", "you're", "on", "your", "own", "with", "hair", "coloring", "advice."]
minions2 = ["minions", "Three", "fast,", "unarmored", "flying", "attackers.", "Roses", "are", "red,", "minions", "are", "blue,", "they", "can", "fly,", "and", "will", "crush", "you!"]
arrows2 = ["arrows", "Arrows", "pepper", "a", "large", "area,", "damaging", "all", "enemies", "hit.", "Reduced", "damage", "to", "Crown", "Towers."]
cannon2 = ["cannon", "Defensive", "building.", "Shoots", "cannonballs", "with", "deadly", "effect,", "but", "cannot", "target", "flying", "troops."]
goblin_gang2 = ["goblin gang", "Spawns", "six", "Goblins", "-", "three", "with", "knives,", "three", "with", "spears", "-", "at", "a", "discounted", "Elixir", "cost.", "It's", "like", "a", "Goblin", "Value", "Pack!"]
skeleton_barrel2 = ["skeleton barrel", "It's", "a", "Skeleton", "party", "in", "the", "sky,", "until", "all", "the", "balloons", "pop...", "then", "it's", "a", "Skeleton", "party", "on", "the", "ground!"]
firecracker2 = ["fire cracker", "Shoots", "a", "firework", "that", "explodes", "upon", "impact,", "damaging", "the", "target", "and", "showering", "anything", "directly", "behind", "it", "with", "sparks.", "This", "is", "what", "happens", "when", "Archers", "get", "bored!"]
royal_delivery2 = ["royal delivery", "No", "need", "to", "sign", "for", "this", "package!", "Dropped", "from", "the", "sky,", "it", "deals", "Area", "Damage", "to", "enemy", "Troops", "before", "delivering", "a", "Royal", "Recruit.", "The", "empty", "box", "is", "also", "handy", "for", "espionage."]
skeleton_dragons2 = ["skeleton dragons", "This", "pair", "of", "skeletal", "scorchers", "deal", "Area", "Damage", "and", "fly", "above", "the", "Arena.", "They,", "also", "play", "a", "mean", "rib", "cage", "xylophone", "duet."]
mortar2 = ["mortar", "Defensive", "building", "with", "a", "long", "range.", "Shoots", "big", "boulders", "that", "deal", "area", "damage,", "but", "cannot", "hit", "targets", "that", "get", "too", "close!"]
tesla2 = ["tesla", "Defensive", "building.", "Whenever", "it's", "not", "zapping", "the", "enemy,", "the", "power", "of", "Electrickery", "is", "best", "kept", "grounded."]
barbarians2 = ["barbarians", "A", "horde", "of", "melee", "attackers", "with", "mean", "mustaches", "and", "even", "meaner", "tempers."]
minion_horde2 = ["minion horde", "Six", "fast,", "unarmored", "flying", "attackers.", "Three's", "a", "crowd", "six", "is", "a", "horde!"]
rascals2 = ["rascals", "Spawns", "a", "mischievous", "trio", "of", "Rascals!", "The", "boy", "takes", "the", "lead,", "while", "the", "girls", "pelt", "enemies", "from", "behind...", "with", "slingshots", "full", "of", "Double", "Trouble", "Gum!"]
royal_giant2 = ["royal giant", "Destroying", "buildings", "with", "his", "massive", "cannon", "is", "his", "job;", "making", "a", "raggedy", "blond", "beard", "look", "good", "is", "his", "passion"]
elite_barbarians2 = ["elite barbarians", "Spawns", "a", "pair", "of", "leveled", "up", "Barbarian.", "They're", "like", "regular", "Barbarians,", "only", "harder,", "better,", "faster", "and", "stronger"]
royal_recruits2 = ["royal recruits", "Deploys", "a", "line", "of", "recruits", "armed", "with", "spears,", "shields", "and", "wooden", "buckets.", "They", "dream", "of", "ponies", "and", "one", "day", "wearing", "metal", "buckets."]
heal_spirit2 = ["heal spirit", "A", "mischievous", "Spirit", "that", "leaps", "at", "enemies,", "dealing", "Damage", "and", "leaving", "behind", "a", "powerful", "healing", "effect", "that", "restores", "Hitpoints", "to", "friendly", "Troops!", "R.I.P.", "Heal", "2017", "-", "2020", "Alas,", "we", "hardly", "used", "ye."]
ice_golem2 = ["ice golem", "He's", "tough,", "targets", "buildings", "and", "explodes", "when", "destroyed,", "slowing", "nearby", "enemies.", "Made", "entirely", "out", "of", "ice...", "or is he?!", "Yes."]
suspicious_bush2 = ["suspicious bush", "This", "invisible", "bush", "skulks", "towards", "the", "nearest", "building.", "Sus.", "If", "Suspicious", "Bush", "reaches", "its", "target", "or", "gets", "destroyed", "by", "a", "spell,", "it", "surprises", "the", "enemy", "with", "Bush", "Goblins!"]
tombstone2 = ["tombstone", "Building", "that", "periodically", "spawns", "Skeletons", "to", "fight", "the", "enemy...", "and", "when", "destroyed,", "spawns", "4", "more", "Skeletons!", "Creepy!"]
mega_minion2 = ["mega minion", "Flying,", "armored", "and", "powerful.", "What", "could", "be", "its", "weakness?!", "Cupcakes."]
dart_goblin2 = ["dart goblin", "Runs", "fast,", "shoots", "far", "and", "chews", "gum.", "How", "does", "he", "blow", "darts", "with", "a", "mouthful", "of", "Double", "Trouble", "Gum?", "Years", "of", "didgeridoo", "lessons"]
earthquake2 = ["earthquake", "Deals", "Damage", "per", "second", "to", "Troops", "and", "Crown", "Towers.", "Deals", "huge", "Building", "Damage!", "Does", "not", "affect", "flying", "units", "(it", "is", "an", "EARTHquake,", "after", "all)."]
elixir_golem2 = ["elixir golem", "Splits", "into", "two", "Elixir", "Golemites", "when", "destroyed,", "which", "splits", "into", "two", "sentient", "Blobs", "when", "defeated.", "Each", "part", "of", "the", "Elixir", "Golem", "gives", "your", "opponent", "some", "Elixir", "when", "destroyed!"]
musketeer2 = ["musketeer", "Don't", "be", "fooled", "by", "her", "delicately", "coiffed", "hair,", "the", "Musketeer", "is", "a", "mean", "shot", "with", "her", "trusty", "boomstick"]
mini_pekka2 = ["mini pekka", "The", "Arena", "is", "a", "certified", "butterfly-free", "zone.", "No", "distractions", "for", "P.E.K.K.A,", "only", "destruction"]
goblin_hut2 = ["goblin hut", "Defensive", "building", "that", "spawns", "Spear", "Goblins", "when", "enemies", "are", "in", "range.", "Don't", "look", "inside...", "you", "don't", "want", "to", "see", "how", "they're", "made"]
goblin_cage2 = ["goblin cage", "When", "the", "Goblin", "Cage", "is", "destroyed,", "a", "Goblin", "Brawler", "is", "unleashed", "into", "the", "Arena!", "Goblin", "Brawler", "always", "skips", "leg", "day."]
fireball2 = ["fireball", "Annnnnd...", "Fireball.", "Incinerates", "a", "small", "area,", "dealing", "high", "damage.", "Reduced", "damage", "to", "Crown", "Towers."]
valkyrie2 = ["valkyrie", "Tough", "melee", "fighter,", "deals", "area", "damage", "around", "her.", "Swarm", "or", "horde,", "no problem!", "She", "can", "take", "them", "all", "out", "with", "a", "few", "spins"]
battle_ram2 = ["battle ram", "Two", "Barbarians", "holding", "a", "big", "log", "charge", "at", "the", "nearest", "building,", "dealing", "significant", "damage", "if", "they", "connect;", "then", "they", "go", "to", "town", "with", "their", "swords!"]
bomb_tower2 = ["bomb tower", "Defensive", "building", "that", "houses", "a", "Bomber.", "Deals", "area", "damage", "to", "anything", "dumb", "enough", "to", "stand", "near", "it."]
hog_rider2 = ["hog rider", "Fast", "melee", "troop", "that", "targets", "buildings", "and", "can", "jump", "over", "the", "river.", "He", "followed", "the", "echoing", "call", "'Hog Riderrrrr'", "all", "the", "way", "through", "the", "Arena", "doors."]
flying_machine2 = ["flying machine", "The", "Master", "Builder", "has", "sent", "his", "first", "contraption", "to", "the", "Arena!", "It's", "a", "fast", "and", "fun", "flying", "machine,", "but", "fragile!"]
battle_healer2 = ["battle healer", "With", "each", "attack", "she", "unleashes", "a", "powerful", "healing", "aura", "that", "restores", "Hitpoints", "to", "herself", "and", "friendly", "Troops"]
zappies2 = ["zappies", "Spawns", "a", "pack", "of", "miniature", "Zap", "machines.", "Who", "controls", "them...?", "Only", "the", "Master", "Builder", "knows."]
furnace2 = ["furnace", "Furnace", "spawns", "one", "Fire", "Spirit", "at", "a", "time", "while", "dealing", "damage", "with", "its", "special", "cauldron", "brew.", "It", "also", "makes", "great", "brick-oven", "pancakes."]
goblin_demolisher2 = ["goblin demolisher", "Boom", "goes", "the", "dynamite!", "Goblin", "Demolisher", "deals", "area", "damage", "and", "explodes", "on", "death.", "At", "low", "health,", "he", "charges", "towards", "the", "nearest", "building."]
giant2 = ["giant", "Slow", "but", "durable,", "only", "attacks", "buildings.", "A", "real", "one-man", "wrecking", "crew!"]
wizard2 = ["wizard", "The", "most", "awesome", "man", "to", "ever", "set", "foot", "in", "the", "Arena,", "the", "Wizard", "will", "blow", "you", "away", "with", "his", "handsomeness...", "and/or", "fireballs."]
inferno_tower2 = ["inferno tower", "Defensive", "building,", "roasts", "targets", "for", "damage", "that", "increases", "over", "time.", "Burns", "through", "even", "the", "biggest", "and", "toughest", "enemies!"]
royal_hogs2 = ["royal hogs", "The", "King's", "personal", "pets", "are", "loose!", "They", "love", "to", "chomp", "on", "apples", "and", "towers", "alike", "-", "who", "let", "the", "hogs", "out?!"]
rocket2 = ["rocket", "Deals", "high", "damage", "to", "a", "small", "area.", "Looks", "really", "awesome", "doing", "it.", "Reduced", "damage", "to", "Crown", "Towers."]
barbarian_hut2 = ["barbarian hut", "Building", "that", "periodically", "spawns", "Barbarians", "to", "fight", "the", "enemy.", "Time", "to", "make", "the", "Barbarians!"]
elixir_pump2 = ["elixir pump", "You", "gotta", "spend", "Elixir", "to", "make", "Elixir!", "This", "building", "makes", "8", "Elixir", "over", "its", "lifetime.", "Does", "not", "appear", "in", "your", "starting", "hand."]
three_musketeers2 = ["three musketeers", "An", "elite", "trio", "of", "powerful,", "independent", "markswomen", "with", "perfectly", "coiffed", "helmets", "and", "bayoneted", "boomsticks.", "They", "slash,", "shoot,", "and", "slay", "in", "the", "name", "of", "justice", "and", "honor"]


desc_list = [skeletons2, fire_spirit2, electro_spirit2, ice_spirit2, goblins2, spear_goblins2, bomber2, bats2, zap2, snowball2, berserker2, knight2, archers2, minions2,
             arrows2, cannon2, goblin_gang2, skeleton_barrel2, firecracker2, royal_recruits2, skeleton_dragons2, mortar2, tesla2, barbarians2, minion_horde2, rascals2,
             royal_giant2, elite_barbarians2, royal_recruits2, heal_spirit2, ice_golem2, suspicious_bush2, tombstone2, mega_minion2, dart_goblin2, earthquake2, elixir_golem2,
             musketeer2, mini_pekka2, goblin_hut2, goblin_cage2, fireball2, valkyrie2, battle_ram2, bomb_tower2, hog_rider2, flying_machine2, battle_healer2, zappies2,
             furnace2, goblin_demolisher2, giant2, wizard2, inferno_tower2, royal_hogs2, rocket2, barbarian_hut2, elixir_pump2, three_musketeers2]#, mirror1, barbarian_barrel1,
             #wall_breakers1, rage1, goblin_curse1, guards1, goblin_barrel1, vines1, tornado1, clone1, void1, baby_dragon1, dark_prince1, freeze1, rune_giant1, poison1,
             #hunter1, goblin_drill1, witch1, balloon1, prince1, electro_dragon1, bowler1, executioner1, cannon_cart1, giant_skeleton1, lightning1, goblin_giant1, xbow1,
             #pekka1, electro_giant1, golem1, log1, royal_ghost1, princess1, miner1, ice_wizard1, bandit1, fisherman1, inferno_dragon1, electro_wizard1, phoenix1,
             #magic_archer1, lumberjack1, night_witch1, mother_witch1, graveyard1, ram_rider1, goblin_machine1, sparky1, spirit_empress1, mega_knight1, lava_hound1,
             #little_prince1, golden_knight1, mighty_miner1, monk1, goblinstein1, archer_queen1, boss_bandit1]


final_stats = []


#=================================================================================================================================================================================


def homescreen():
   print("============================================= ")
   print(" _____                   _          _ _       ")
   print("|  __ \                 | |        | | |      ")
   print("| |__) |___  _   _  __ _| | ___  __| | | ___  ")
   print("|  _  // _ \| | | |/ _` | |/ _ \/ _` | |/ _ \ ")
   print("| | \ \ (_) | |_| | (_| | |  __/ (_| | |  __/ ")
   print("|_|  \_\___/ \__, |\__,_|_|\___|\__,_|_|\___| ")
   print("              __/ |                           ")
   print("             |___/                            ")
   print("==============================================")


def guess_the_card():
   print("======================   CLASSIC   ======================")
   # rankings (lowest -> highest)
   types_list = ["troop", "spell", "building"]
   targets_list = ["ground", "air + ground", "building"]
   rarity_list = ["common", "rare", "epic", "legendary", "champion"]
   ranges_list = ["melee:short", "melee:medium", "melee:long", "ranged", "area effect"]
   speeds_list = ["slow", "medium", "fast", "very fast", "N/A"]


   # assign mystery card
   card = randint(0, (len(card_names) - 1))
   card_name = card_names[card]
   if card_elixirs[card] != "?":
       card_elixir = card_elixirs[card]
   else:
       card_elixir = "?"
   card_rarity = rarity_list[card_rarities[card]]
   card_type = types_list[card_types[card]]
   card_target = targets_list[card_targets[card]]
   card_range = ranges_list[card_ranges[card]]
   card_hitspeed = card_hitspeeds[card]
   card_speed = speeds_list[card_speeds[card]]


   tries = 0
   while True:
       guess = input("\nguess the card   ")
       print("")
       while guess not in card_names:
           guess = input("\ncard entered not in card pool! try again:   ")
       print("")
       card_gid = card_names.index(guess)
       if card_names[card_gid] != card_name:
           print(f"CARD:       |  X  {card_names[card_gid]}")
       else:
           print(f"CARD:       |  ✓  {card_names[card_gid]}")
       sleep(0.35)
       if card_elixirs[card_gid] != card_elixir:
           if card_elixirs[card_gid] == "?" or card_elixirs[card_gid] < card_elixir:
               print(f"ELIXIR:     |  ↑  {card_elixirs[card_gid]}")
           else:
               print(f"ELIXIR:     |  ↓  {card_elixirs[card_gid]}")
       else:
           print(f"ELIXIR:     |  ✓  {card_elixirs[card_gid]}")
       sleep(0.35)
       if card_rarities[card_gid] != card_rarities[card]:
           if card_rarities[card_gid] > card_rarities[card]:
               print(card)
               print(f"RARITY:     |  ↓  {rarity_list[card_rarities[card_gid]]}")
           else:
               print(f"RARITY:     |  ↑  {rarity_list[card_rarities[card_gid]]}")
       else:
           print(f"RARITY:     |  ✓  {rarity_list[card_rarities[card_gid]]}")
       sleep(0.35)
       if card_types[card_gid] != card_types[card]:
           print(f"CARD TYPE:  |  X  {types_list[card_types[card_gid]]}")
       else:
           print(f"CARD TYPE:  |  ✓  {types_list[card_types[card_gid]]}")
       sleep(0.35)
       if card_targets[card_gid] != card_targets[card]:
           print(f"TARGET:     |  X  {targets_list[card_targets[card_gid]]}")
       else:
           print(f"TARGET:     |  ✓  {targets_list[card_targets[card_gid]]}")
       sleep(0.35)
       if card_ranges[card_gid] != card_ranges[card]:
           print(f"CARD RANGE: |  X  {ranges_list[card_ranges[card_gid]]}")
       else:
           print(f"CARD RANGE: |  ✓  {ranges_list[card_ranges[card_gid]]}")
       sleep(0.35)
       if card_hitspeeds[card_gid] != card_hitspeeds[card]:
           if card_hitspeeds[card_gid] > card_hitspeeds[card]:
               print(f"HIT SPEED:  |  ↓  {card_hitspeeds[card_gid]} seconds")
           else:
               print(f"HIT SPEED:  |  ↑  {card_hitspeeds[card_gid]} seconds")
       else:
           print(f"HIT SPEED:  |  ✓  {card_hitspeeds[card_gid]} seconds")
       sleep(0.35)
       tries += 1
       if card_names[card_gid] == card_name:
           break
   print("")
   print(f"Congratulations! You correctly guessed the card, {card_name} in {tries} tries.")
   pinput = input("Do you want to play again? (y/n) ")
   if pinput.lower() == "y":
       final_stats.append(f"CLASSIC    :  {tries} TRIES")
       choose_gamemode()
   else:
       final_stats.append(f"CLASSIC    :  {tries} TRIES")
       end_game()
       quit()


def emoji_guess_mode():
   card = randint(0, (len(emoji_list) - 1))
   card_today = emoji_list[card]
   card_iterate = 0
   card_display = []
   tries = 1
   print(card)
   print("======================   EMOJIS   ======================\n")
   while True:
       if card_iterate <= 3:
           card_display.append(card_today[card_iterate])
           card_iterate += 1
       else:
           pass


       print(f"\n{card_display}")
       guess_emoji = input("\nGuess the card based off the emojis  ")
       if guess_emoji == card_today[4]:
           sleep(0.15)
           print(f"\nCARD:      |     ✔     {guess_emoji}")
           sleep(0.15)
           break
       else:
           sleep(0.15)
           print(f"\nCARD:      |     X     {guess_emoji}")
           sleep(0.15)
           tries += 1


   print(f"\nYou guessed the card: {card_today[4]} in {tries} tries!")
   pinput = input("\nwould you like to play again? (y/n)   ")
   if pinput == "y":
       final_stats.append(f"EMOJI      :  {tries} TRIES")
       choose_gamemode()
   else:
       final_stats.append(f"EMOJI      :  {tries} TRIES")
       end_game()
       quit()


def desc_guess_mode():
   card_today = desc_list[randint(0, (len(desc_list) - 1))]
   desc = []
   word_pos = []
   temp = ""
   tries = 0
   for x in range(0, (len(card_today)-1)):
       for y in card_today[x+1]:
           temp += "_"
       desc.append(temp)
       temp = ""
   for y in range(1, len(card_today)):
       word_pos.append(y)


   while True:
       for x in desc:
           print(x, end=" ")
           sleep(0.1)
       print("")
       guess_desc = input("\nguess the card  ")
       if guess_desc == card_today[0]:
           break
       else:
           if len(word_pos) != 0:
               word_replace = randint(0, (len(word_pos)-1))
               desc[word_pos[word_replace]-1] = card_today[word_pos[word_replace]]
               word_pos.remove(word_pos[word_replace])
               tries += 1
           else:
               pass


   print("")
   for x in card_today:
       if x == card_today[0]:
           pass
       else:
           print(x, end=" ")
           sleep(0.1)
   print(f"\nYou guessed the card: {card_today[0]} in {tries+1} tries!")
   pinput = input("\nwould you like to play again? (y/n)   ")
   if pinput == "y":
       final_stats.append(f"DESCRIPTION:  {tries} TRIES")
       choose_gamemode()
   else:
       final_stats.append(f"DESCRIPTION:  {tries} TRIES")
       end_game()
       quit()


def choose_gamemode():
   homescreen()
   personality = ["Excellent choice!", "Nice taste!", "Great!", "Nice,", "OK!", "Good choice,", "Neat,", "My favourite as well!"]
   print("------------- Welcome! What game mode would you like to play? -------------")
   print("1) CLASSIC:     |            every guess gives you a stat clue             ")
   print("2) EMOJI:       |          guess the card from a set of 4 emojis           ")
   print("3) DESCRIPTION: |         guess the card based of the description          ")
   pinput = input().lower()
   if pinput == "classic" or pinput == "1":
       pinput = input(f"\n{personality[randint(0, len(personality)-1)]} Would you like the card pool printed (y/n)?   \n").lower()
       if pinput == "y":
           print("============================= CARD POOL =============================\n")
           for x in range(len(card_names)):
               print(card_names[x])
           print("")
       else:
           pass
       guess_the_card()


   elif pinput == "emoji" or pinput == "2":
       pinput = input(f"\n{personality[randint(0, len(personality) - 1)]} Would you like the card pool printed (y/n)?   \n").lower()
       if pinput == "y":
           print("============================= CARD POOL =============================\n")
           for x in range(len(card_names)):
               print(card_names[x])
           print("")
       else:
           pass
       emoji_guess_mode()


   elif pinput == "description" or pinput == "3":
       pinput = input(
           f"\n{personality[randint(0, len(personality) - 1)]} Would you like the card pool printed (y/n)?   \n").lower()
       if pinput == "y":
           print("============================= CARD POOL =============================\n")
           for x in range(len(card_names)):
               print(card_names[x])
           print("")
       else:
           pass
       desc_guess_mode()


   else:
       print("Sorry, the game mode is not available.")


def end_game():
   print("\nThank you for playing!")
   print("#Share your stats! :")
   for x in final_stats:
       print(x, end="\n")


choose_gamemode()
