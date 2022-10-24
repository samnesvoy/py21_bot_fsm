from aiogram.utils.helper import Helper, ListItem,HelperMode


class MyStates(Helper):
    mode = HelperMode.CamelCase

    STATE_0 = ListItem()
    STATE_1 = ListItem()
    STATE_2 = ListItem()
    STATE_3 = ListItem()
    STATE_4 = ListItem()




if __name__ == '__main__':
    print(MyStates.all())
