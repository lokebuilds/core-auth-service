class WebSocketConnectionManager:
    def __init__(self):
        self.active_connections = set()

    async def disconnect(self, websocket):
        self.active_connections.discard(websocket)
