def taomlar_boyicha_turlar(menyu):
    taom_turlari = {}
    
    for taom, info in menyu.items():
        taom_turi = info['taom_turi']
        
        if taom_turi not in taom_turlari:
            taom_turlari[taom_turi] = []
        
        taom_turlari[taom_turi].append(taom)
    
    return taom_turlari

menyu = {
    'Osh': {'narx': 20000, 'taom_turi': 'milliy'},
    'Shashlik': {'narx': 15000, 'taom_turi': 'gril'},
    'Lagmon': {'narx': 18000, 'taom_turi': 'milliy'}
}

natija = taomlar_boyicha_turlar(menyu)

print(natija)
