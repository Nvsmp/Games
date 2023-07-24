extends Node2D

@export var speed:int = 400
@export var dano:int = 1
@export var vida:int = 1
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.
	$AnimatedSprite2DEnemy.play("walking")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	position.x -= 1
	if vida <= 0:
		queue_free()
	
