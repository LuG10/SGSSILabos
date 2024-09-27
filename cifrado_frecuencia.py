from collections import Counter
def descifrarCodigo():
    frecuencia=['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 't', 'c', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f', 'v', 'j', 'ñ', 'z', 'x', 'k', 'w']
    mensaje= "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE  AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK  HKCZJOI OKEJSZCNHE"
#miramos la cantidad de letras de cada tipo que hay(primero quitamos separaciones)
    mensajeSinEspacios= mensaje.replace(" ", "")
    contador = Counter(mensajeSinEspacios)

#inicializamos los elementos internos necesarios para descifrar el mensaje
    mensajeCorrecto = False
    i=0

#bucle de descifrado
    while not mensajeCorrecto:
        ayuda=True
        print(contador)
        #pedimos la letra mas utilizada al usuario
        letrasMasFrecuentes= input('\n Cual es la letra mas utilizada: \n')
        mensaje=mensaje.replace(letrasMasFrecuentes.upper(),frecuencia[i])
        #del contador[i]
        print("\n")
        print(mensaje)
        i=i+1
        while ayuda == True:
            pregunta= input(' ¿Identificas alguna letra? (s/n) \n')
            if pregunta== 's' or pregunta=='S':
                letraCambio=input(' letra a cambiar: \n')
                letraRemplazo=input(' su cambio: \n')
                mensaje=mensaje.replace(letraCambio.upper(),letraRemplazo)
                print(mensaje)
            else:
                ayuda=False
        pregunta= input('\n ¿Esta el mensaje descifrado? (s/n) \n')
        if pregunta== 's' or pregunta=='S': 
            mensajeCorrecto= True
    
descifrarCodigo()