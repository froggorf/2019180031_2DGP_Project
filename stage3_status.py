from pico2d import *
import play_state
import stage
import item
import game_world
import enemy

stage2_w = 7751
stage2_h = 1913

def eventbox_create_box():
    for fb in play_state.footBlock:
        game_world.remove_object(fb)

    for i in range(13):
        play_state.footBlock += [stage.FootBlock(4123-62*(i+1),stage2_h-691-62,4123-(62*i),stage2_h-691)]

    game_world.add_objects(play_state.footBlock,1)
    game_world.add_collision_group(play_state.yoshi, play_state.footBlock, 'yoshi:footBlock')
    game_world.add_collision_group(play_state.enemies, play_state.footBlock, 'enemies:footBlock')





def input_object_to_game_world():
    play_state.groundRect = [
        #stage.myRect(0, 0,233,474),
        stage.myRect(0,0,211,818),
        stage.myRect(0,0,3775,219),




        stage.myRect(6409,0,6409+1293,212)

    ]

    play_state.stairRect = [
        stage.myRect(732,0,732+455,247),
        stage.myRect(765,0,765+405,274),
        stage.myRect(988,0,988+152,306),
        stage.myRect(1015,0,1015+110,326),

        stage.myRect(1733,0,1733+317,252),
        stage.myRect(1755,0,1755+242,280),
        stage.myRect(1783,0,1783+169,301),
        stage.myRect(1805,0,1805+118,324),

    ]

    play_state.ceilingBlock = [

    ]
    play_state.footBlock = [
        # stage.FootBlock(1921, 3263 - 2494, 1921 + 62, 3263 - 2494 + 62),
        stage.FootBlock(1202 + 62 * 0, 1280 - 630 - 62, 1202 + 62 * 1, 1280 - 630),
        stage.FootBlock(1202 + 62 * 1, 1280 - 630 - 62, 1202 + 62 * 2, 1280 - 630),
        stage.FootBlock(1202 + 62 * 2, 1280 - 630 - 62, 1202 + 62 * 3, 1280 - 630),

        stage.FootBlock(1574 + 62 * 0, 1280 - 446 - 62, 1574 + 62 * 1, 1280 - 446),

        stage.FootBlock(1857 + 62 * 0, 1280 - 122 - 62, 1857 + 62 * 1, 1280 - 122),

        stage.FootBlock(2319 + 62 * 0, 1280 - 544 - 62, 2319 + 62 * 1, 1280 - 544),
        stage.FootBlock(2319 + 62 * 1, 1280 - 544 - 62, 2319 + 62 * 2, 1280 - 544),
        stage.FootBlock(2319 + 62 * 2, 1280 - 544 - 62, 2319 + 62 * 3, 1280 - 544),

        stage.FootBlock(2690 + 62 * 0, 1280 - 399 - 62, 2690 + 62 * 1, 1280 - 399),

        stage.FootBlock(3174 + 62 * 0, 1280 - 285 - 62, 3174 + 62 * 1, 1280 - 285),

        stage.FootBlock(3801 + 62 * 0, 1280 - 333 - 62, 3801 + 62 * 1, 1280 - 333),
        stage.FootBlock(3801 + 62 * 1, 1280 - 333 - 62, 3801 + 62 * 2, 1280 - 333),
        stage.FootBlock(3801 + 62 * 2, 1280 - 333 - 62, 3801 + 62 * 3, 1280 - 333),
        stage.FootBlock(3801 + 62 * 3, 1280 - 333 - 62, 3801 + 62 * 4, 1280 - 333),
        stage.FootBlock(3801 + 62 * 4, 1280 - 333 - 62, 3801 + 62 * 5, 1280 - 333),
        stage.FootBlock(3801 + 62 * 5, 1280 - 333 - 62, 3801 + 62 * 6, 1280 - 333),
        stage.FootBlock(3801 + 62 * 6, 1280 - 333 - 62, 3801 + 62 * 7, 1280 - 333),
        stage.FootBlock(3801 + 62 * 7, 1280 - 333 - 62, 3801 + 62 * 8, 1280 - 333),
        stage.FootBlock(3801 + 62 * 8, 1280 - 333 - 62, 3801 + 62 * 9, 1280 - 333),
        stage.FootBlock(3801 + 62 * 9, 1280 - 333 - 62, 3801 + 62 * 10, 1280 - 333),



        #마지막 블럭들
        stage.FootBlock(4300, 1280-1050-62, 4300 + 62, 1280-1050),
        stage.FootBlock(4700, 1280 - 950 - 62, 4700 + 62, 1280 - 950),
        stage.FootBlock(6100, 1280 - 1200 - 62, 6100 + 62, 1280 - 1200),


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
    play_state.eventbox =[
        #item.EventBox(4600,1500, eventbox_create_box)
    ]


    play_state.finishLine = stage.myRect(6817, 0, 6817 + 500, stage2_h - 1359 - 80 + 1)
    from random import randint
    play_state.enemies = [
        #enemy.Flower(739, 1913-1405),
        enemy.Rocket(7500-randint(0,50), 100+randint(-10,10)),
        enemy.Rocket(7500-randint(0,50), 200+randint(-10,10)),
        enemy.Rocket(7500-randint(0,50), 300+randint(-10,10)),
        enemy.Rocket(7500-randint(0,50), 400+randint(-10,10)),
        enemy.Rocket(7500-randint(0,50), 500+randint(-10,10)),
        enemy.Rocket(7500-randint(0,50), 600+randint(-10,10)),
        enemy.Rocket(7500-randint(0,50), 700+randint(-10,10)),
        enemy.Rocket(7500-randint(0,50), 800+randint(-10,10)),

        enemy.Rocket(7500 - randint(0, 50), 150 + randint(-10, 10)),
        enemy.Rocket(7500 - randint(0, 50), 350 + randint(-10, 10)),
        enemy.Rocket(7500 - randint(0, 50), 550 + randint(-10, 10)),
        enemy.Rocket(7500 - randint(0, 50), 750 + randint(-10, 10)),

        enemy.Rocket(6500, 110,3780),
        enemy.Rocket(6500, 0,3780),

    ]
    play_state.game_over_line = [
        stage.myRect(3780,0,3780+2628,1),
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
    game_world.add_objects(play_state.eventbox,1)

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
    game_world.add_collision_group(play_state.yoshi, play_state.game_over_line, 'yoshi:gameover')


    game_world.add_collision_group(play_state.enemies, play_state.groundRect, 'enemies:groundRect')
    game_world.add_collision_group(play_state.enemies, play_state.stairRect, 'enemies:stairRect')
    game_world.add_collision_group(play_state.enemies, play_state.ceilingBlock, 'enemies:ceilingBlock')
    game_world.add_collision_group(play_state.enemies, play_state.footBlock, 'enemies:footBlock')
    game_world.add_collision_group(play_state.enemies, play_state.largeBlock, 'enemies:largeBlock')

    play_state.stage_bgm = load_music('resource\\sound\\stage3_sound.mp3')
    play_state.stage_bgm.set_volume(32)
    play_state.stage_bgm.repeat_play()