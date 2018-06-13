def insert_element(string, group, element):

    # Calculate the number of elements to be inserted
    num_com = (len(string)-1)//group
    # Index indicates the position where to insert the element
    index = (-1)*group
    # Calculate the element lenght
    l_element = len(element)

    for i in range(num_com):
        string = string[:index] + element + string[index:]
        index = index - (group+l_element)

    return string


