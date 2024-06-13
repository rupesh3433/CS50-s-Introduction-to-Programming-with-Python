#pip install and use this module ------ use join method to join words
import inflect
p = inflect.engine()

def main():
    input_lists = []
    while True:
        try:
            word_input = input("Name: ")
            input_lists.append(word_input)
        except EOFError:
            join_words_using_adieu(input_lists)
            break

def join_words_using_adieu(input_lists):
    adieu_string = "Adieu, adieu, to "
    joined_list = p.join(input_lists)
    print(adieu_string + joined_list)

main()
