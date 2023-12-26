import keyboard
import requests
import time

# Este Script, detecta el la pistola lector de codigos de barra 
def scan_codes():
    codigo = ""
    while True:
        evento = keyboard.read_event(suppress=True)

        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name == "enter":
                break
            else:
                codigo += evento.name
    return codigo

#Envia el Código obtenido por Metodo POST 
def enviar_codigo(codigo):
    url = "http://127.0.0.1:8000/api/leer-codigo/" #URL API
    codigo_sin_ultimo_digito = codigo[:-1] # Le quita el ultimo numero
    codigo_con_cero = "0" + codigo_sin_ultimo_digito # Le agrega un 0 al principio
    data = {"codigo": codigo_con_cero}
    
    try:
        response = requests.post(url, data=data) #Envia los datos en formato JSON
        response.raise_for_status()  # Genera una excepción para códigos de estado HTTP no exitosos


        # Muestra la respuesta de la solicitud
        print("Respuesta de la solicitud POST:", response.text)
        print("Código de barras enviado exitosamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud POST: {e}", response.text)

if __name__ == "__main__":
    #Si se deasea que este un un bucle, quitar el comentario al while
    #while True:
        codigo_barras = scan_codes()
        enviar_codigo(codigo_barras)
        time.sleep(1)  # aqui se puede ajustar el tiempo en segundos, 1 = 1 segundo
