import play_state
import stage
import item
import game_world
import enemy

stage2_w = 7751
stage2_h = 1913

def input_object_to_game_world():
    play_state.groundRect = [
        #stage.myRect(0, 0,233,474),
        #stage.myRect(199,0,199+398,458)
        stage.myRect(3210,0,3210+15,657),
        stage.myRect(4375,0,4375+9,650),
        stage.myRect(4866,0,4866+152,649),
        stage.myRect(4982,0,4982+324,820),
        stage.myRect(4123,stage2_h-691-58,4123+224,stage2_h-691),
        stage.myRect(4584,stage2_h-1087-57,4584+395,stage2_h-1087),
        stage.myRect(5422, stage2_h - 960 - 135, 5422 + 64, stage2_h - 960),
        stage.myRect(5469, stage2_h - 1017 - 56, 5469 + 731, stage2_h - 1017),
        stage.myRect(6077, stage2_h - 1019 - 132, 6077+147, stage2_h - 1019),
        stage.myRect(5885,0,5885+162,834),
        stage.myRect(6038,0,6038+1713,471),
        # stage.myRect()
    ]

    play_state.stairRect = [
        # stage.myRect(830, 0, 880, 528),


        stage.myRect(0, 0, 233, 474),
        stage.myRect(199, 0, 199 + 398, 458),
        stage.myRect(617,0,617+237,481),
        stage.myRect(817, 0, 817 + 728, 420),
        stage.myRect(1535,0,1535+736,495),
        stage.myRect(2248,0,2248+464,548),
        stage.myRect(2653,0,2653+398,612),
        stage.myRect(2947,0,2947+146,644),
        stage.myRect(3008,0,3008+91,703),
        stage.myRect(3052,0,3052+12,763),
        stage.myRect(3109,0,3109+101,662),
        stage.myRect(3200,0,3200+431,535),
        stage.myRect(3380,0,3380+808,589),
        stage.myRect(3434,0,3434+421,648),
        stage.myRect(4064,0,4064+311,652),
        stage.myRect(4389,0,4389+113,518),
        stage.myRect(4388,0,4388+321,477),
        stage.myRect(4690,0,4690+385,534),
        stage.myRect(5033,0,5033+234,886),
        stage.myRect(5077,stage2_h-969-99,5077+358,stage2_h-969),
        stage.myRect(5336, stage2_h - 939 - 40, 5336 + 122, stage2_h - 939),
        stage.myRect(5336, stage2_h - 939 - 40, 5336 + 122, stage2_h - 939),
        stage.myRect(5383, stage2_h - 909 - 25, 5383 + 43, stage2_h - 909),
        stage.myRect(6087, stage2_h - 986 - 29, 6087 + 96, stage2_h - 986),
        # stage.myRect(),
    ]

    play_state.ceilingBlock = [

        stage.myRect(6042, stage2_h - 1231 - 84, 6042+42, stage2_h - 1231),
        stage.myRect(6057, stage2_h - 1173 - 97, 6057 + 80, stage2_h - 1173),
        stage.myRect(6105, stage2_h - 1114 - 85, 6105 + 115, stage2_h - 1114),
        # stage.myRect(2960, 870, 3000, 1100),

    ]
    play_state.footBlock = [
        # stage.FootBlock(1921, 3263 - 2494, 1921 + 62, 3263 - 2494 + 62),

    ]
    play_state.largeBlock = [
        # stage.LargeBlock(2045, 3263 - 2494, 2045 + 62, 3263 - 2494 + 62),

    ]
    play_state.jumpBlock = [
        # stage.JumpBlock(500, 508, 500 + 62, 508 + 62, 101),

    ]
    play_state.coins = [
        # item.Coin(1170, 700),
    ]

    play_state.finishLine = stage.myRect(6817,stage2_h-1359-80,6817+104,stage2_h-1359)

    play_state.enemies = [enemy.Flower(700,700),enemy.Flower(100,700),enemy.Flower(1948,1000),enemy.Flower(3600,1500)]


    game_world.add_objects(play_state.largeBlock, 1)
    game_world.add_objects(play_state.groundRect,1)
    game_world.add_objects(play_state.stairRect, 1)
    game_world.add_objects(play_state.ceilingBlock, 1)
    game_world.add_objects(play_state.footBlock, 1)
    game_world.add_objects(play_state.jumpBlock, 1)
    game_world.add_objects(play_state.coins, 1)
    game_world.add_object(play_state.finishLine, 1)
    game_world.add_objects(play_state.enemies, 1)

    #충돌체크 그룹 추가
    game_world.add_collision_group(play_state.yoshi, play_state.groundRect, 'yoshi:groundRect')
    game_world.add_collision_group(play_state.yoshi, play_state.stairRect, 'yoshi:stairRect')
    game_world.add_collision_group(play_state.yoshi, play_state.ceilingBlock, 'yoshi:ceilingBlock')
    game_world.add_collision_group(play_state.yoshi, play_state.footBlock, 'yoshi:footBlock')
    game_world.add_collision_group(play_state.yoshi, play_state.largeBlock, 'yoshi:largeBlock')
    game_world.add_collision_group(play_state.yoshi, play_state.jumpBlock, 'yoshi:jumpBlock')
    game_world.add_collision_group(play_state.yoshi, play_state.coins, 'yoshi:coins')
    game_world.add_collision_group(play_state.yoshi, play_state.finishLine, 'yoshi:finishLine')
    game_world.add_collision_group(play_state.yoshi, play_state.enemies, 'yoshi:enemies')


    game_world.add_collision_group(play_state.enemies, play_state.groundRect, 'enemies:groundRect')
    game_world.add_collision_group(play_state.enemies, play_state.stairRect, 'enemies:stairRect')
    game_world.add_collision_group(play_state.enemies, play_state.ceilingBlock, 'enemies:ceilingBlock')
    game_world.add_collision_group(play_state.enemies, play_state.footBlock, 'enemies:footBlock')
    game_world.add_collision_group(play_state.enemies, play_state.largeBlock, 'enemies:largeBlock')