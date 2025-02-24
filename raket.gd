extends RigidBody2D





@export var thrust_force: float = 500     # Hvor hurtigt raketten flyver
@export var rotation_speed: float = 3.0     # Hvor hurtigt raketten roterer

func _physics_process(delta: float) -> void:
	
	
	# Håndter rotation
	if Input.is_action_pressed("move_left"):
		rotation -= rotation_speed * delta
		
	if Input.is_action_pressed("move_right"):
		rotation += rotation_speed * delta
		

	# Håndter thrust (motorens kraft)
	if Input.is_action_pressed("thrust"):
		# Udregn retningen: Vi starter med vektoren (0, -1), der peger opad
		# og roterer den med rakettens rotation for at få den aktuelle retning.
		var force_direction = Vector2(0, -1).rotated(rotation)
# Påfør impulsen ved rakettens centrum (Vector2.ZERO)
		apply_force(Vector2.ZERO, force_direction * thrust_force * delta)
		
