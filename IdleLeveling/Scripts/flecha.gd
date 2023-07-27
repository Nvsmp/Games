extends Area2D

@export var speed:int = 300
var direcao:Vector2 
var dano:int = 1
var screen_size 

# Called when the node enters the scene tree for the first time.
func _ready():
	screen_size = get_viewport_rect().size

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	position += direcao * speed * delta
	#print(direcao)
	#print(position)
	if position.x < -1000 or position.x > 1000 or position.y < -1000 or position.y > 1000:
		queue_free()
	
func set_dir(dir,pos_torre, angulo):
	rotation = angulo
	direcao = dir - pos_torre
	direcao = direcao.normalized()

func _on_area_entered(area):
	area.vida -= dano
	if area.vida <= 0:
		area.queue_free()
	queue_free()
