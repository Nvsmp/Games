extends Area2D
#"<Freed Object>"
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
var last_enemy_pos: Vector2
var angulo_flecha:float

#ONREADY
func _ready():
	pass # Replace with function body.
	$AnimatedSprite2D.play("1")
	$AnimatedSprite2D/Arqueiro.play("idle")

#PROCESS
func _process(delta):
	if atacando and $AnimatedSprite2D/Arqueiro.animation == "idle":
		$AnimatedSprite2D/Arqueiro.play("attack_right")
	elif !atacando and $AnimatedSprite2D/Arqueiro.animation == "attack_right":
		$AnimatedSprite2D/Arqueiro.play("idle")
	else:
		$AnimatedSprite2D/Arqueiro.play("idle")
	if !array_inimigos.is_empty():
		update_inimigos()
	if !array_inimigos.is_empty():
		if !tiro_em_cd and !str(array_inimigos[0]) == "<Freed Object>":
			atacando = true
			var alvo:Vector2 = array_inimigos[0].position
			var flecha = flecha_scene.instantiate()
			flecha.position = Vector2.ZERO
			angulo_flecha = position.angle_to(alvo)
			#print(angulo_flecha)
			flecha.set_dir(alvo, position, angulo_flecha)
			add_child(flecha)
			tiro_em_cd = true
			$TimerCD.start()
		else:
			atacando = false
	
	
	
#FUNCOES
func update_inimigos():
	if str( array_inimigos[0] ) == "<Freed Object>":
		array_inimigos.remove_at(0)
		
func uparVida()->void:
	vida_torre_max += 5
	
func _on_timer_regen_vida_timeout():
	vida_torre += regen_vida
	if vida_torre > vida_torre_max:
		vida_torre = vida_torre_max

func _on_range_area_entered(area):
	#print("Inimigo entrou no range da torre")
	array_inimigos.append(area)

func _on_area_2d_hitbox_area_entered(area):
	vida_torre -= area.dano
	area.queue_free()
	update_inimigos()
	

func _on_timer_cd_timeout():
	tiro_em_cd = false
	
