extends Area2D

@export var vida_torre_max:int = 10
@export var vida_torre:int = 10
@export var regen_vida:int = 1
@export var preco_up_regen_vida:int = 1
@export var preco_up_vida_max:int = 1
@export var xp:int = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_area_entered(area):
	print(area.dano)
	vida_torre -= area.dano
	
func uparVida()->void:
	vida_torre_max += 5


func _on_timer_regen_vida_timeout():
	vida_torre += regen_vida
	if vida_torre > vida_torre_max:
		vida_torre = vida_torre_max
