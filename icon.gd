extends Sprite2D



# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


if body.name = "Raket":
func _on_Platform_body_entered(body):
		# Her kan du tjekke body.linear_velocity og body.rotation for at afgøre landingsstatus
	if body.linear_velocity.length() < 50 and abs(body.rotation) < 0.1:
		print("Sikker landing!")
	else:print("Crash!")
