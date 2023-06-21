from pynput import mouse

cliques = 0

def on_click(x, y, button, pressed):
    global cliques
    
    if not pressed and button == mouse.Button.middle:
        print(x, y,)
        cliques += 1
        
        if cliques >= 10:
            # Parar o código
            return False
        
with mouse.Listener(on_click=on_click) as coordenadas:
    coordenadas.join()