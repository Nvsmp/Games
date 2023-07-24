extends Area2D

@export var flecha_scene: PackedScene
@export var vida_torre_max:int = 10
@export var vida_torre:int = 10
@export var regen_vida:int = 1
@export var preco_up_regen_vida:int = 1
@export var preco_up_vida_max:int = 1
@export var xp:int = 0
var atacando:bool = false
var array_inimigos:Array = []
@export var tiro_em_cd:bool = false
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
	#printt("Array de inimigos: "+ str(array_inimigos))
	if !array_inimigos.is_empty():
		atacando = true
		if str(array_inimigos[0]) == "<Freed Object>":
			array_inimigos.remove_at(0)
		if !tiro_em_cd:
			#print("tiro")
			var flecha = flecha_scene.instantiate()
			flecha.position = Vector2.ZERO
			flecha.set_dir(array_inimigos[0].position, position)
			add_child(flecha)
			tiro_em_cd = true
			$TimerCD.start()
			
			
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
	vida_torre -= area.dano





func _on_timer_cd_timeout():
	tiro_em_cd = false
