from pico2d import *
import play_state
import stage
import item
import game_world
import enemy
def input_object_to_game_world():
    play_state.groundRect = [
        stage.myRect(0, 0, 832, 512),
        stage.myRect(1024, 0, 1536, 512),
        stage.myRect(1680, 608, 1820, 650),
        stage.myRect(1820, 0, 2368, 608),
        stage.myRect(2371, 0, 2373, 837),
        stage.myRect(3010, 700, 3015, 1000),
        stage.myRect(2880, 940, 3000, 1100),
        stage.myRect(3000, 1060, 3340, 1080),
        stage.myRect(3253, 0, 4044, 530),
        stage.myRect(3250, 0, 3253, 998),
        stage.myRect(3270, 980, 3385, 1045),
        stage.myRect(4042, 0, 4045, 1150),
        stage.myRect(3905, 1272, 3910, 1345),
        stage.myRect(4080, 1282, 4308, 1334),
        stage.myRect(4290, 1219, 4798, 1274),
        stage.myRect(4749, 1284, 4755, 1420),
        stage.myRect(4544, 1600, 4570, 1727),
        stage.myRect(4787, 1693, 5307, 1728),
        stage.myRect(5121, 2735, 5188, 2890),
        stage.myRect(5260, 1729, 5317, 2680),
        stage.myRect(5333, 3262 - 404, 6142, 3262 - 381)
    ]

    play_state.stairRect = [
        stage.myRect(830, 0, 880, 528),
        stage.myRect(864, 0, 896, 560),
        stage.myRect(896, 0, 928, 592),
        stage.myRect(928, 0, 960, 560),
        stage.myRect(1568, 0, 1576, 592),
        stage.myRect(1624, 0, 1626, 688),
        stage.myRect(2450, 0, 2450, 907),
        stage.myRect(2510, 0, 2564, 950),
        stage.myRect(2606, 0, 2608, 900),
        stage.myRect(2646, 0, 2648, 850),
        stage.myRect(2688, 0, 2690, 800),
        stage.myRect(2690, 0, 2850, 770),
        stage.myRect(2850, 0, 2950, 735),
        stage.myRect(2995, 1130, 3005, 1150),
        stage.myRect(2950, 1120, 3050, 1130),
        stage.myRect(3976, 1347, 3990, 1402),
        stage.myRect(4028, 1352, 4035, 1445),
        stage.myRect(4066, 1347, 4090, 1402),
        stage.myRect(4634, 1685, 4723, 1780),
        stage.myRect(5204, 3262 - 392, 5299, 3262 - 343)
    ]
    play_state.ceilingBlock = [
        stage.myRect(2960, 870, 3000, 1100),
        stage.myRect(2880, 920, 3000, 1100),
        stage.myRect(3904, 1200, 4020, 1300),
        stage.myRect(4020, 1150, 4100, 1250),
        stage.myRect(4708, 1419, 4767, 1503),
        stage.myRect(4647, 1466, 4705, 1551),
        stage.myRect(4589, 1532, 4647, 1614),
        stage.myRect(4552, 1673, 4609, 1590),
        stage.myRect(5136, 2660, 5256, 2783)
    ]
    play_state.footBlock = [
        stage.FootBlock(1921, 3263 - 2494, 1921 + 62, 3263 - 2494 + 62),
        stage.FootBlock(1983, 3263 - 2494, 1983 + 62, 3263 - 2494 + 62),
        stage.FootBlock(2107, 3263 - 2494, 2107 + 62, 3263 - 2494 + 62),
        stage.FootBlock(2169, 3263 - 2494, 2169 + 62, 3263 - 2494 + 62),
        stage.FootBlock(3460, 3263 - 2558, 3460 + 62, 3263 - 2558 + 62),
        stage.FootBlock(3522, 3263 - 2558, 3522 + 62, 3263 - 2558 + 62),
        stage.FootBlock(3646, 3263 - 2558, 3646 + 62, 3263 - 2558 + 62),
        stage.FootBlock(3708, 3263 - 2558, 3708 + 62, 3263 - 2558 + 62),
    ]
    play_state.largeBlock = [
        stage.LargeBlock(2045, 3263 - 2494, 2045 + 62, 3263 - 2494 + 62),
        stage.LargeBlock(3584, 3263 - 2558, 3584 + 62, 3263 - 2558 + 62)
    ]
    play_state.jumpBlock = [
        stage.JumpBlock(4432, 1275, 4432 + 62, 1275 + 62, 75),
        stage.JumpBlock(4994, 1720, 4994 + 62, 1720 + 62, 115)
    ]
    play_state.coins = [
        item.Coin(1170, 700),
        item.Coin(1270, 700),
        item.Coin(1370, 700),
        item.Coin(2000, 1250),
        item.Coin(2000, 1050),
        item.Coin(2100, 1250),
        item.Coin(2100, 1050),
        item.Coin(2550, 1050),
        item.Coin(2630, 1150),
        item.Coin(2750, 1200),
        item.Coin(2850, 1150),
        #
        # item.Coin(3350, 1200),
        # item.Coin(3425, 1300),
        # item.Coin(3550, 1410),
        # item.Coin(3675, 1500),

        item.Coin(4445, 1500),
        item.Coin(4445, 1700),
        item.Coin(4580, 1800),

        item.Coin(5012, 1900),
        item.Coin(5012, 2160),
        item.Coin(5012, 2420),
        item.Coin(5012, 2680),
        item.Coin(5012, 2900),
        item.Coin(5150, 3050)
    ]
    play_state.finishLine = stage.myRect(5747, 2898, 6139, 2900)

    play_state.enemies = [
        #enemy.Flower(700,700),
        enemy.Flower(1146,3264-2660-80),
        enemy.Flower(1962, 3264 - 2569-80),
        enemy.Flower(3489,3264 - 2610-80),
        enemy.Flower(4542,3264-1880-80)

        ]


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

    play_state.stage_bgm = load_music('resource\\sound\\stage1_sound.mp3')
    play_state.stage_bgm.set_volume(32)
    play_state.stage_bgm.repeat_play()