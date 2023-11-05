import re
# Home work 9

telefone_directori_dict = {} # Створюємо словник для збрігання даних

def input_error(func):    # Функція декоратор приймає функцію із hundlera і  обробляє винятки
     
    def inner(volume):
        try:
            return func(volume)
            
        except ValueError:
            return 'Incorrect command'
        except KeyError:
            return 'Give me name please'
        except IndexError:
            return  'Give me name and phone please'
        
    return inner   

# Функціі обробки команд hundlera
@input_error
def greeting (vol=None):                     
    if not vol:  
        return "How can I help you?"
    raise ValueError
     

@input_error
def add_entry(vol):
    operands = vol.split()
    # print(vol[0])
    if  not telefone_directori_dict.get(operands[0]):
        telefone_directori_dict[operands[0]] = operands[1]
        return 'Ok'  
        
    raise IndexError
    

@input_error
def change_entry(vol):
    operands = vol.split()
    # print (vol)
    if  telefone_directori_dict.get(operands[0]):
        telefone_directori_dict[operands[0]] = operands[1]
        return 'Ok'  
        
    raise KeyError
    


    
@input_error
def output_entry(vol):
    if telefone_directori_dict.get(vol):
        return telefone_directori_dict.get(vol)
    
    raise KeyError

@input_error
def output_all_entry(vol=None):
    if not vol:  
        return telefone_directori_dict
    raise ValueError
    
    
@input_error
def bye(vol = None):
    if not vol:  
        return "Good bye!"
    raise ValueError

     

hundler = {'hallo': greeting , 'add' : add_entry, 'change' : change_entry, 'phone': output_entry, 'show all' : output_all_entry, 'good bye' : bye, 'close' : bye, 'exit' : bye}




def parser_hundler(str):        #Функція Парсер команд
    key_hundler = str.lower()
    for key in hundler.keys():
        if key_hundler.startswith(key):
            result = re.search(key, key_hundler)
            second_index = result.span()[1]
            if key_hundler == key or str[second_index] == ' ':
                return [key, str[second_index:].strip()]
            
     
 
def main():
    while True:
        print ('>>>', end = '')
        hundler_string = input ()
        
        command_str = parser_hundler(hundler_string)
         
        if command_str:
            command = command_str[0]
            operand = command_str[1]
               
            if hundler.get(command) == bye and not operand:
                print (hundler.get(command)(operand))
                break
            if  hundler.get(command) == output_all_entry:
                output = hundler.get(command)(operand)
                print ('-'*32)
                print (f"|{'Name': ^15}|{'Phone': ^15}|")
                print ('-'*32)
                for key, volume in output.items():
                    print (f"|{key : <15}|{volume : <15}|") 
                print ('-'*32)    
            else:
                print(hundler.get(command)(operand))
        else:
            print ('Command is missing')    
        
            

if __name__ == '__main__':
    main()
