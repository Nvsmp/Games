extends Area2D

@export var vida_torre_max:int = 10
@export var vida_torre:int = 10
@export var regen_vida:int = 1
@export var preco_up_regen_vida:int = 1
@export var preco_up_vida_max:int = 1
@export var xp:int = 0
var atacando:bool = false
var array_inimigos:Array = []
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.
	$AnimatedSprite2D.play("1")
	$AnimatedSprite2D/Arqueiro.play("idle")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if atacando:
		$AnimatedSprite2D/Arqueiro.play("attack_left")
	else:
		$AnimatedSprite2D/Arqueiro.play("idle")
	printt("Array de inimigos: "+ str(array_inimigos))
	if !array_inimigos.is_empty():
		atacando = true
		if str(array_inimigos[0]) == "<Freed Object>":
			array_inimigos.remove_at(0)
	else:
		atacando = false

	
func uparVida()->void:
	vida_torre_max += 5


func _on_timer_regen_vida_timeout():
	vida_torre += regen_vida
	if vida_torre > vida_torre_max:
		vida_torre = vida_torre_max


func _on_range_area_entered(area):
	print("Inimigo entrou no range da torre")
	array_inimigos.append(area)


func _on_area_2d_hitbox_area_entered(area):
	area.queue_free()
