from pyngrok import ngrok

ngrokTunnel = ngrok.connect(8000)
print(f"Public url is {ngrokTunnel.public_url}")
nest

