extends StaticBody2D





func _on_body_entered(_body):
	if _body is RigidBody2D:  # Tjekker om det er raketten
		if _body.linear_velocity.length() < 50 and abs(_body.rotation_degrees) < 10:
			print("Sikker landing!")
		else:
			print("Crash!")
