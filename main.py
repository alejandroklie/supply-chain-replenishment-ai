import pandas as pd
import math

def calculate_reorder_points():
    print("--- Starting AI Supply Chain Optimization ---")
    
    # 1. Simulación de datos de inventario actual de la marca (Sportswear)
    inventory_data = {
        'Product_ID': ['BND-01', 'BND-02', 'GK-01', 'GK-02'],
        'Product_Name': ['High-Waist Leggings', 'Sports Bra Pro', 'Oversized Hoodie', 'Running Shorts'],
        'Current_Stock': [120, 45, 15, 210],
        'Average_Daily_Sales': [8.5, 4.2, 3.1, 12.0],
        'Supplier_Lead_Time_Days': [25, 25, 30, 20], # Tiempos de envío estimados desde Asia
        'Safety_Stock_Days': [7, 7, 10, 5] # Margen de seguridad para evitar quiebres
    }
    
    df = pd.DataFrame(inventory_data)
    
    # 2. Lógica Predictiva de Operaciones
    # Reorder Point (ROP) = (Ventas Diarias Promedio * Tiempo de Entrega) + Stock de Seguridad
    df['Safety_Stock_Units'] = (df['Average_Daily_Sales'] * df['Safety_Stock_Days']).apply(math.ceil)
    df['Reorder_Point'] = ((df['Average_Daily_Sales'] * df['Supplier_Lead_Time_Days']) + df['Safety_Stock_Units']).apply(math.ceil)
    
    # 3. Alertas de reabastecimiento automáticas
    df['Action_Required'] = df.apply(lambda row: '⚠️ ORDER NOW' if row['Current_Stock'] <= row['Reorder_Point'] else '✅ Stock OK', axis=1)
    
    # 4. Calcular días restantes de inventario antes de quedar en cero
    df['Days_Until_Stockout'] = (df['Current_Stock'] / df['Average_Daily_Sales']).round(1)
    
    # Mostrar resultados en consola de forma organizada
    print("\nOperational Replenishment Report:")
    print(df[['Product_ID', 'Product_Name', 'Current_Stock', 'Reorder_Point', 'Days_Until_Stockout', 'Action_Required']])
    
    # Guardar reporte optimizado en un archivo CSV para la administración
    df.to_csv('replenishment_report.csv', index=False)
    print("\nReport successfully generated and saved as 'replenishment_report.csv'")

if __name__ == "__main__":
    calculate_reorder_points()
