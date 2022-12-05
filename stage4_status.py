from pico2d import *
import play_state
import stage
import item
import game_world
import enemy

stage2_w = 7751
stage2_h = 1913


event_1 = False
event_2 = False
def event_box_del1():
    global event_1,event_2
    if event_2:
        for rect in play_state.footBlock:
            game_world.remove_object(rect)
        play_state.footBlock=[]
    else:
        event_1=True
    pass

def event_box_del2():
    global event_1,event_2
    if event_1:
        print('!')
        for rect in play_state.footBlock:
            game_world.remove_object(rect)
        play_state.footBlock = []
    else:
        event_2=True
    pass




def input_object_to_game_world():
    global event_1,event_2
    event_1=False
    event_2 = False
    play_state.groundRect = [
        #stage.myRect(0, 0,233,474),
        stage.myRect(0,0,1532,212), #밑벽
        stage.myRect(0,0,102,6000), #왼쪽벽
        stage.myRect(0,6000-212,2000,6000),#윗벽
        stage.myRect(1131,0,1131+105,5257), #오른쪽벽

        stage.myRect(513,6000-5414-105,513+720,6000-5414),#첫번쨰

        stage.myRect(0,6000-5096-106,720,6000-5096),

        stage.myRect(315,6000-4630-105-50,315+616,6000-4630-50),
        stage.myRect(516,6000-4188-107-70,516+719,6000-4188-70),

        stage.myRect(0,6000-3295-108,717,6000-3295),
        stage.myRect(514,6000-2851-107-20,514+719,6000-2851-20),

        stage.myRect(0,6000-1443-103,723,6000-1443),
        stage.myRect(512,6000-1058-101,512+1026,6000-1058),

        stage.myRect(1131,6000-739-106,1131+1083,6000-739),
        stage.myRect(1437,6000-820-343,1437+101,6000-820),


    ]

    play_state.stairRect = [


    ]

    play_state.ceilingBlock = [

    ]
    play_state.footBlock = [

        stage.FootBlock(1131, 6000 - 675 + 62 * 6, 1131 + 62, 6000 - 675 + 62 * 7),
        stage.FootBlock(1131, 6000 - 675 + 62 * 5, 1131 + 62, 6000 - 675 + 62 * 6),
        stage.FootBlock(1131, 6000 - 675 + 62 * 4, 1131 + 62, 6000 - 675 + 62 * 5),
        stage.FootBlock(1131, 6000 - 675 + 62 * 3, 1131 + 62, 6000 - 675 + 62 * 4),
        stage.FootBlock(1131, 6000 - 675 + 62 * 2, 1131 + 62, 6000 - 675 + 62 * 3),
        stage.FootBlock(1131, 6000 - 675 + 62 * 1, 1131 + 62, 6000 - 675 + 62 * 2),
        stage.FootBlock(1131, 6000 - 675 + 62 * 0, 1131 + 62, 6000 - 675 + 62 * 1),
        stage.FootBlock(1131, 6000 - 675 + 62 * -1, 1131 + 62, 6000 - 675 + 62 * 0),

    ]
    play_state.largeBlock = [
        # stage.LargeBlock(2045, 3263 - 2494, 2045 + 62, 3263 - 2494 + 62),

    ]
    play_state.jumpBlock = [
        stage.JumpBlock(1030, 6000-4196-62, 1030 + 62, 6000-4196, 101),
        stage.JumpBlock(881, 6000 - 2809 - 62, 881 + 62, 6000 - 2809, 120),
    ]
    play_state.coins = [
        # item.Coin(1170, 700),




    ]
    play_state.eventbox =[
        item.EventBox(950,6000-764, event_box_del1),
        item.EventBox(233, 6000 - 818, event_box_del2)
    ]


    play_state.finishLine = stage.myRect(1464,6000-717-14,1464,6000-717)
    from random import randint
    play_state.enemies = [
        enemy.Flower(1270, 6000-950),
        enemy.Flower(1270, 6000 - 950),
        enemy.Flower(1270, 6000 - 950),
        enemy.Flower(1270, 6000 - 950),

    ]
    play_state.game_over_line = [
        stage.Lava(105,0,105+1024,1)
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
    game_world.add_objects(play_state.game_over_line,1)

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

    play_state.stage_bgm = load_music('resource\\sound\\stage4_sound.mp3')
    # play_state.stage_bgm.set_volume(32)
    # play_state.stage_bgm.repeat_play()