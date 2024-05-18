class RequestMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Get the request object from the scope
        request = scope.get("http_request")
        print(request)
        # Attach the request object to the scope
        scope["request"] = request
        # Call the inner application
        
        return await self.inner(scope, receive, send)