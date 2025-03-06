from pyautocad import Autocad, APoint
import time
 
# Connect to AutoCAD
acad = Autocad(create_if_not_exists=True)

# INTRODUCIR PARAMETROS PARA REINTENTOS
delay= 0.1
retry=2





def get_string_from_user(MSG):
    # AutoCAD command to ask for a string using the 'getstring' method
    for i in range(retry):
        try:
            user_input = acad.ActiveDocument.Utility.GetString(True, MSG)
            return user_input
        except Exception as e:
            time.sleep(delay)
            acad.prompt(f"Error processing extracting options or numeric vlaue: {e}")

        



# Function to perform arithmetic operations on text values
def perform_arithmetic_operations(delay, retry, x, y):
# Loop through all Text entities in the drawing
    selection = acad.get_selection()
    
    for obj in selection:
        for i in range(retry):
            
            try:
    # Extract the current text value
                text_value = obj.TextString
    # Check if the text is a number (skip text that isn't numeric)

                number = float(text_value)

                    
    # Example arithmetic operations
                if y=="1":
                    result_add = round(number + x, 2)
                    new_text = str(result_add)
                                
                elif y=="2":
                    result_subtract = round(number - x, 2)
                    new_text = str(result_subtract)
                    
                elif y=="3":
                    result_multiply = round(number * x, 2)
                    new_text = str(result_multiply)
                    
                elif y=="4":

                    result_divide = round(number / x, 2)
                    new_text = str(result_divide)

                else:
                    acad.prompt("no se ha seleccionado un numero valido")

                
                obj.TextString = new_text
                break
                


            except Exception as e:
                time.sleep(delay)
                acad.prompt(f"Error processing text object: {e}")

















y = str(get_string_from_user("SELECCIONAR MODO: 1-SUMAR, 2-RESTAR, 3-MULTIPLICAR, 4-DIVIDIR"))

time.sleep(delay)

x = float(get_string_from_user("VALOR NUMERICO"))

time.sleep(delay)

perform_arithmetic_operations(delay, retry, x, y)
