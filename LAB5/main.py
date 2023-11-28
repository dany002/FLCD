from grammar import Grammar
from parser import Parser

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    grammar1 = Grammar("grammar1.txt")
    grammar2 = Grammar("grammar2.txt")

    parser1 = Parser(grammar1)
    parser2 = Parser(grammar2)

    parser1.add_productions_to_file("( int + int )")
    parser2.add_productions_to_file("< and or and >")

    # print()
    parser1.run_tests()
    grammar1.print_s()
    grammar1.print_terminals()
    grammar1.print_productions()
    grammar1.print_nonterminals()
    grammar1.print_productions_for_nonterminal("A")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/