import time

def verificar_lampadas():
   
    lampadas = {
        'A': 'desligada',
        'B': 'desligada',
        'C': 'desligada'
    }

    interruptores = {
        '1': 'desligado',
        '2': 'desligado',
        '3': 'desligado'
    }

    
    interruptores['1'] = 'ligado'
    print("Interruptor 1 ligado por 3 minutos...")
    time.sleep(3)  

   
    interruptores['1'] = 'desligado'
    interruptores['2'] = 'ligado'

   
    lampadas['A'] = 'acesa' if interruptores['1'] == 'ligado' else 'apagada'
    lampadas['B'] = 'acesa' if interruptores['2'] == 'ligado' else 'apagada'
    
   
    print("Verificando lampadas...")

   

    for lampada, estado in lampadas.items():
        print(f"Lampada {lampada}: {estado}")

   
    print("Interruptor 1 controla a lampada A.")
    print("Interruptor 2 controla a lampada B.")
    print("Interruptor 3 controla a lampada C.")

verificar_lampadas()
