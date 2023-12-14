integer = int(500)
float_variable = float(1.5)
string_single_Line = str("Hi single line")
string_mutli_line = str("""Hi
multi
line""")
boolean = True

list_variables = [integer,float_variable,string_single_Line,string_mutli_line,boolean]

for type_variable in list_variables:
    if True == boolean:
        print(type_variable)
    else:
        print("No output possible")
        break

print("\n")

def print_all_variables(integer,float_variable,string_single_Line,string_mutli_line,boolean):
    print(str(integer)
          + "\n" +
          str(float_variable)
          + "\n" +
          str(boolean)
          + "\n" +
          string_single_Line
          + "\n" +
          string_mutli_line
          )
print_all_variables(integer,float_variable,string_single_Line,string_mutli_line,boolean)
