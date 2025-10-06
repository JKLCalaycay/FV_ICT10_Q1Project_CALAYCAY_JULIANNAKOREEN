from pyscript import document, display 

'''this is what i used to solve for the price of the order'''

def solving_forprice (e): #e for COMPUTATION
    item1 = float(document.getElementById("input1").value)
    item2 = float(document.getElementById("input2").value)
    item3 = float(document.getElementById("input3").value)
    item4 = float(document.getElementById("input4").value)
    item5 = float(document.getElementById("input5").value)


    total = 0
    for i in range(1, 6):
        checkbox = document.getElementById(f"input{i}")
        if checkbox.checked:
            total += float(checkbox.value)

    display(f"Total Price: PHP{total:.2f}", target="Grade")

    '''this is what i used to get the information of the client in my website'''
    
def getting_info (e): #e for COMPUTATION
    Name = str(document.getElementById("name1").value)
    Addrs = str(document.getElementById("address2").value)
    Telno = str(document.getElementById("telno3").value)

    if not Name or not Addrs or not Telno:
        display("Youre as silly as the Cheshire Cat! You must input something in the textbox!")
        return

    display(f"""Order information: 
        \nName: {Name} 
        \nAddress: {Addrs} 
        \nTelephone Number: {Telno}""", target="message")