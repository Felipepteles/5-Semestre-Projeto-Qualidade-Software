def calcular_taxa_entrega(distancia):
    base = 5.0
    taxa_extra = 2.0
    distancia_fixa = 3

    if distancia < 0:
        raise ValueError("Distância não pode ser negativa")
        
    if distancia <= distancia_fixa:
        return base
        
    km_adicional = distancia - distancia_fixa
    return base + (km_adicional * taxa_extra)