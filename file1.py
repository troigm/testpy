# Test para github file 1.
# -*- coding: utf-8 -*-


def write_times(times,text):
    """
    Function for print x times, one text
    :param times: the times that you see
    :param text: the text that you want print
    """
    for x in range(1, times):
        print "Nº %s: " % str(x), str(text)


if __name__ == '__main__':
    write_times(10, 'Hola')
