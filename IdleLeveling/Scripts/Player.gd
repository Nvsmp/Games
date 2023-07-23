extends Area2D
var virado_direita:bool = true
var speed:int = 400
var screen_size

# Called when the node enters the scene tree for the first time.
func _ready():
	screen_size = get_viewport_rect().size


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var vetor_aceleracao = Vector2.ZERO
	if Input.is_action_pressed("direita"):
		vetor_aceleracao.x += 1
	if Input.is_action_pressed("esquerda"):
		vetor_aceleracao.x -= 1
	if Input.is_action_pressed("cima"):
		vetor_aceleracao.y -= 1
	if Input.is_action_pressed("baixo"):
		vetor_aceleracao.y += 1
	if vetor_aceleracao.length() > 0:
		vetor_aceleracao = vetor_aceleracao.normalized() * speed
	if vetor_aceleracao.x < 0:
		virado_direita = false
	elif vetor_aceleracao.x > 0:
		virado_direita = true
	if vetor_aceleracao.length() == 0:
		$AnimatedSprite2D.play("idle")
		$AnimatedSprite2D.flip_h = !virado_direita
	else:
		$AnimatedSprite2D.play("run")
	position += vetor_aceleracao * delta
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)
	printt("Vetor Aceleracao: ", vetor_aceleracao)


