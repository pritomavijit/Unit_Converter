import pandas as pd


data = {
    'unit': ['meter', 'kilometer', 'centimeter', 'millimeter', 'inch', 'foot', 'yard', 'mile'],
    'to_meter': [1, 1000, 0.01, 0.001, 0.0254, 0.3048, 0.9144, 1609.34]
}
conversion_df = pd.DataFrame(data)

def convert_units(value, from_unit, to_unit):
    try:
    
        from_factor = conversion_df.loc[conversion_df['unit'] == from_unit, 'to_meter'].values[0]
        to_factor = conversion_df.loc[conversion_df['unit'] == to_unit, 'to_meter'].values[0]
        
       
        value_in_meters = value * from_factor
        converted_value = value_in_meters / to_factor
        
        return converted_value
    except IndexError:
        return "Invalid unit. Please check your input."

def main():
    print("Welcome to the Measuring Unit Converter!")
    print("Available units: meter, kilometer, centimeter, millimeter, inch, foot, yard, mile")
    
    
    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the source unit: ").strip().lower()
        to_unit = input("Enter the target unit: ").strip().lower()
        
        
        result = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
