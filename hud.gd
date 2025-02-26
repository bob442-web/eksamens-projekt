extends CanvasLayer

# Notifies `Main` node that the button has been pressed
signal start_game





func new_game() -> void:

	$HUD.update_score(score)
	$HUD.show_message("Get Ready")
