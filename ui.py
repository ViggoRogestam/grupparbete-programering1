class Ui:
    def __init__(self, ui_width: int):
        self.ui_width = ui_width

    def print_line(self):
        print('-' * self.ui_width)

    def print_dot(self):
        print('*' * self.ui_width)

    def print_header(self, header):
        arg = header
        print('.: {header} :.'.format(header=arg).center(self.ui_width))

    def print_choices(self, *choice):
        choice_list = choice
        print('-' * self.ui_width)
        for i, value in enumerate(choice_list):
            i += 1
            print('| {number} - {choice}'.format(choice=value, number=i))

