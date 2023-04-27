from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.title = 'blocks'                # The window title
window.borderless = True               # Show a border
window.fullscreen = False             # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = False  
editor_camera = EditorCamera(enabled=False, ignore_paused=True)

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.
class Grass(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=0,
            scale=1,
            texture='texture1',
            double_sided = True,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.white,
        )

class Dirt(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=0,
            scale=1,
            texture='texture2',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.white,
        )

class Stone(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=0,
            scale=1,
            texture='texture3',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.white,
        )
        
for z in range(10):
    for x in range(10):
        grass = Grass(position=(x,10,z))
        stone = Stone(position=(x,-1,z))
        stone = Stone(position=(x,-2,z))
        stone = Stone(position=(x,-3,z))
        stone = Stone(position=(x,-4,z))
        stone = Stone(position=(x,-5,z))

for z in range(10):
    for x in range(10):
        for y in range(10):
            dirt = Dirt(position=(x,y,z))

e = Entity(model="cube", scale=1, collider='box')
e.position = (3,10.5,0)

def pause_input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)

def input(key):
    if key == 'q':
        e.position = (0,0,0)
        e.texture = ('grass.png')
    if key == 'e':
        e.position = (10,10,10)
    if key == '1':
        f = open('block.txt', 'w')
        f.write('grass')
        # close the file
        f.close()
    if key == '2':
        f = open('block.txt', 'w')
        f.write('dirt')
        # close the file
        f.close()
    if key == '3':
        f = open('block.txt', 'w')
        f.write('stone')
        # close the file
        f.close()
    if key == 'left mouse down':
        f = open('block.txt', 'r')
        block_type = f.read()
        # close the file
        f.close()
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit and block_type == 'dirt':
            Dirt(position=hit_info.entity.position + hit_info.normal)
        if hit_info.hit and block_type == 'grass':
            Grass(position=hit_info.entity.position + hit_info.normal)
        if hit_info.hit and block_type == 'stone':
            Stone(position=hit_info.entity.position + hit_info.normal)
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

player = FirstPersonController()

app.run()
