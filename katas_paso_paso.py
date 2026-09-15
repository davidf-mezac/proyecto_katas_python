def calcular_compra():
    try:
        # 1. Solicita al usuario el precio original
        precio_original = float(input("Ingresa el precio original del artículo (€): "))
        
        # 2. Pregunta si tiene cupón
        # .strip().lower() limpia espacios extra y pasa a minúsculas la respuesta
        tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ").strip().lower()
        
        # 6. Uso de if, elif y else
        if tiene_cupon == "sí" or tiene_cupon == "si":
            # 3. Solicita el valor del cupón
            valor_cupon = float(input("Ingresa el valor del cupón (€): "))
            
            # 4. Aplica el descuento si es mayor a cero
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
                
                # Pequeña validación extra: evitar que la tienda nos deba dinero
                if precio_final < 0:
                    precio_final = 0
                    
                # 5. Muestra precio final con descuento
                print(f"Descuento aplicado. Total a pagar: {precio_final}€")
            else:
                print(f"Cupón no válido (debe ser > 0). Total a pagar: {precio_original}€")
                
        elif tiene_cupon == "no":
            # 5. Muestra precio final sin descuento
            print(f"No hay descuento. Total a pagar: {precio_original}€")
            
        else:
            print(f"Respuesta no reconocida. Total a pagar: {precio_original}€")
            
    except ValueError:
        print("Error: Por favor, ingresa solo valores numéricos para los precios.")

# Prueba Kata 41:
print("\n--- Kata 41 ---")
calcular_compra()
