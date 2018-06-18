from InsertElement import insert_element
from InputInteger import inputInteger

def main():

    # Default: Takes an integer and return a string representation of that integer with commas separating groups of 3 digits
    number = str(inputInteger())
    print(insert_element(number, 3, ','))

    # Extended: Takes a string and return the string separating the characters by an element in groups
    '''
    string = str("Enter the string: ")
    element = str(input("Enter the separator element: "))
    group = int(input("Separate in groups of: "))

    # Prints the return string
    print(insert_element(string,group,element))
    '''

if __name__ == "__main__":
    main()
