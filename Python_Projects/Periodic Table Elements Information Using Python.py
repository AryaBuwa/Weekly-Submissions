#importing necessary libraries
import periodictable

# defining the function to get information
def get_periodic_table_element_info(symbol):
    print(f"Looking for symbol : '{symbol}'")
    element = getattr(periodictable, symbol, None)
    
# Writing the logic
    if element:
        print(f"Element: {element.name}")
        print(f"Symbol: {element.symbol}")
        print(f"Atomic Number: {element.number}")
        print(f"Atomic Mass: {element.mass} u")
    else :
        print("Element not found in the Periodic Table. ")

# Example : 

if __name__ == "__main__":

# Added exception handling for continuous function   
    while True:
        try:
            symbol = input("Enter the Elemnt: (or Type 'exit' to quit.): ")
            if symbol.lower() == 'exit':
                break
            symbol = symbol.capitalize()
            get_periodic_table_element_info(symbol)
        except Exception as e:
            print(f"Error: {e}")
    