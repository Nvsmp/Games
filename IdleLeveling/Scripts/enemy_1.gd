extends Node2D

@export var speed:int = 10
@export var dano:int = 1
@export var vida:int = 1

var dir:Vector2
# Called when the node enters the scene tree for the first time.
func _ready():
	$AnimatedSprite2DEnemy.play("walking")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if dir != null:
		position += dir * speed * delta
	if vida <= 0:
		queue_free()
		
func set_dir(vetor_alvo) -> void:
	dir = vetor_alvo - position
	dir = dir.normalized()
	
	
	
