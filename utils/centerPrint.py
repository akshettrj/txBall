def print_centered_text(text, columns, color=None):
	if not color:
		text_centering_buffer = " " * int((columns - len(text)) / 2)
		print(text_centering_buffer, end="")
		print(text)

	else:
		text_centering_buffer = " " * int((columns - len(text)) / 2)
		print(text_centering_buffer, end="")
		print(color + text)
