extends RigidBody2D


# Called when the node enters the scene tree for the first time.
func _ready():
	var mob_tipos = $AnimatedSprite2D.sprite_frames.get_animation_names()
	$AnimatedSprite2D.play(mob_tipos[randi() % mob_tipos.size() ])
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_visible_on_screen_notifier_2d_screen_exited():
	queue_free()
	
