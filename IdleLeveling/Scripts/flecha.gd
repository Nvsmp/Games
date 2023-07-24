extends Area2D

@export var speed:int = 600
var direcao:Vector2 
var dano:int = 1

# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	position += direcao * speed * delta
	#print(direcao)
	
func set_dir(dir,pos_torre):
	direcao = dir - pos_torre
	direcao = direcao.normalized()



func _on_area_entered(area):
	print("hit")
	area.vida -= dano
	queue_free()
