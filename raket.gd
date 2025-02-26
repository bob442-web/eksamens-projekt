extends RigidBody2D

@export var thrust_force: float = 500.0  # Hvor hurtigt raketten flyver
@export var rotation_speed: float = 3.0  # Hvor hurtigt raketten roterer

func _physics_process(delta: float) -> void:
	# Håndter rotation
	if Input.is_action_pressed("move_left"):
		rotation -= rotation_speed * delta
		
	if Input.is_action_pressed("move_right"):
		rotation += rotation_speed * delta

	# Håndter thrust (motorens kraft)
	if Input.is_action_pressed("thrust"):
		var force_direction = Vector2(0, -1).rotated(rotation)  # Retningen raketten peger
		apply_impulse(force_direction * thrust_force * delta)  # Påfør impulsen
