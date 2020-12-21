extends AnimatedSprite

func _on_RightButton_pressed():
	position.x += 64
	position.x = clamp(position.x, 160, 608)
func _on_LeftButton_pressed():
	position.x -= 64
	position.x = clamp(position.x, 160, 608)
func _on_UpButton_pressed():
	position.y -= 64
	position.y = clamp(position.y, 160, 608)
func _on_DownButton_pressed():
	position.y += 64
	position.y = clamp(position.y, 160, 608)




# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
