functions are used to perfrom a repetive tast, while writing a function must maxium do one major task, 
'''
def functionName():
""" 
Must have the function body in it, function body must contain a doc string in it, so that it helps to know and print what does function does and what args it expect as an input.
when you use help(function_name) it shows us what does it does. 
"""


positional argumnets must come before the keyword arguments. ex: functionName(postition_args, key_word_args) functionName(server="nginx", running)
positional Argumnets:
like functionName(nginx, running)
Keyword Arguments:(service_Name="nginx", status="running")

default_peramaetrers: we need to pass the default parametr so when no value is provide the function uses the default valeus for evaluation 

python with 

modules = socket, random 

In range() when working with the larger values we can work with the _ to impove the readablity range(100_000_00)


range loads the numbers on the iteration, it only stores the numbers only start, stop and step of the range(start, stop, step)
but when range combined with list list(range(100_00_00)) it will load all the value which is memoery insentive so we need to use range incase of memory optimization.
