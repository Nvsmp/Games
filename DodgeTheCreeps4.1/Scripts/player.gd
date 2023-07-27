extends Area2D

signal hit
@export var speed:int = 400
var screen_size 
var movCima:bool = false
var movBaixo:bool = false
var movEsquerda:bool = false
var movDireita:bool = false

# Called when the node enters the scene tree for the first time.
func _ready():
	screen_size = get_viewport_rect().size
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var velocidade = Vector2.ZERO 
	if Input.is_action_pressed("direita"):
		velocidade.x += 1
	if Input.is_action_pressed("esquerda"):
		velocidade.x -= 1
	if Input.is_action_pressed("cima"):
		velocidade.y -= 1
	if Input.is_action_pressed("baixo"):
		velocidade.y += 1 
		
	if velocidade.length() > 0:
		velocidade = velocidade.normalized() * speed
		$AnimatedSprite2D.play()
	else:
		$AnimatedSprite2D.stop()
	
	position += velocidade * delta
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)
	
	#printt("delta: ", delta, "velocidade: ", velocidade, "position: ",position)	
	
	if velocidade.x != 0:
		$AnimatedSprite2D.animation = "walk"
		$AnimatedSprite2D.flip_h = velocidade.x < 0
	elif velocidade.y != 0:
		$AnimatedSprite2D.animation = "up"
		$AnimatedSprite2D.flip_v = velocidade.y > 0
	else:
		$AnimatedSprite2D.flip_v = false


func _on_body_entered(body):
	hide()
	hit.emit()
	$CollisionShape2D.set_deferred("disabled", true)
func start(pos):
	position = pos
	show()
	$CollisionShape2D.disabled = false
