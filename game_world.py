objects = [[] for _ in range(4)] #보이는 세계이다. 보이게 하려면 add_objects했다.


#충돌의 세계 충돌의 세계는 남아있으므로 여기서도 지워야한다.
collision_pairs = {} #딕셔너리  'boy: balls' : [ [boy],[ball1,ball2,,,,]]




def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()

# fill here
def add_collision_pair(group, a= None, b=None): #a와 b사이에 충돌 검사가 필요하다
    if group not in collision_pairs:
        print(f'Added new group{group}')
        collision_pairs[group] = [[], []] #초기화 리스트오브리스트로 두개의 리스트로
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o) #충돌도 날려야한다.
            del o #객체자체를 날려줘야한다.
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()



# fill here
def remove_collision_object(o): #게임월드리스트 오브젝트 리스트에서 지운것이다. 지워야할 곳이 또 있다.
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)



def collide(a,b):
    la,ba,ra,ta = a.get_bb()
    lb,bb,rb,tb = b.get_bb()

    if la > rb : return False  #충돌이 안되는 경우들
    if ra < lb : return False
    if ta < bb : return False
    if ba > tb: return False

    return True


def handle_collisions():
    for group, pairs in collision_pairs.items(): #각각의 키벨류가 나온다 group과 pair로.
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

