def on_on_chat():
    pass
player.on_chat("run", on_on_chat)
def on_chat_chunk():
    position = player.position()

    start_x = int(position.get_value(Axis.X) // 16) * 16
    start_z = int(position.get_value(Axis.Z) // 16) * 16

    current_y = position.get_value(Axis.Y)

    blocks.fill(
        BEACON,
        world(start_x, 0, start_z),
        world(start_x + 16, current_y - 1, start_z + 16),
        FillOperation.REPLACE
    )
#player.on_chat("2", on_chat_chunk)
player.on_item_interacted(ENCHANTED_APPLE, on_chat_chunk)
