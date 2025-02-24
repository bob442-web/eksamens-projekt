extends RigidBody2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

 # Kraften fra raketmotoren # Hvor hurtigt raketten roterer
  # Håndter rotation


func _physics_process(delta):
	export var rotation_speed: float = 3

if Input.is_action_pressed("rotate_left"):
		rotation -= rotation_speed * delta
if Input.is_action_pressed("rotate_right"):
		rotation += rotation_speed * delta

		
export var thrust_force: float = 500
	# Håndter thrust
	if Input.is_action_pressed("thrust"):
		# Beregn kraftens retning baseret på rakettens rotation
		var force_direction = Vector2(0, -1).rotated(rotation)
		apply_impulse(Vector2.ZERO, force_direction * thrust_force * delta)
