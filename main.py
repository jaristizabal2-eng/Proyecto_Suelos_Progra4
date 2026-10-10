from ui.consola import pedir_datos_usuario, mostrar_tabla
from api.datos import obtener_datos_excel, calcular_medianas

def main():
    departamento, municipio, cultivo, limite = pedir_datos_usuario()
    
    # Nombre exacto de tu archivo excel
    ruta_excel = "resultado_laboratorio_suelo.xlsx" 
    
    df_filtrado, mensaje = obtener_datos_excel(ruta_excel, departamento, municipio, cultivo, limite)
    
    if df_filtrado is not None:
        med_ph, med_p, med_k = calcular_medianas(df_filtrado)
        mostrar_tabla(df_filtrado, med_ph, med_p, med_k)
    else:
        print(f"\n[!] {mensaje}")

if __name__ == "__main__":
    main()