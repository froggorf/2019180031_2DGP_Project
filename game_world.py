# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[], []]

collision_group = dict()
#'boy:ball' : [(boy),(ball1, ball2, ball3, ...)] 와 같은 정보가 담김

# yoshi
# -largerBlock(stageState)
# -footBlock(stageState)
# -ceilingBlock(stageState)
# -jumpBlock(stageState)
# -groundRect(stageState)
# -stairRect(stageState)
#
# -enemy
#
# -coin(item)
#
# -finishLine(stageState)
#
#
# enemy - 지형들


def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return

def all_objects():
    for layer in objects:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()
    global collision_group
    collision_group = dict()

def add_collision_group(a,b,group):
    if group not in collision_group:
        # print('New Group Made')
        collision_group[group] = [[], []]
    if a:
        if type(a) == list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)

    if b:
        if type(b) == list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)


def all_collision_pairs():
    #collision_group 딕셔너리에서 각 리스트로부터 페어를 만들어서 보내줌
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group

def remove_collision_object(o):
    for pairs in collision_group.values(): #key:value 에서 value에 해당되는것만 가져옴

        while o in pairs[0]:
            pairs[0].remove(o)
        while o in pairs[1]:
            pairs[1].remove(o)
