
MAX =  1000
MIN = -1000

class Line:

    def __init__(self,a,b):

        self.a = a
        self.b = b

    def __lt__(self, other):

        if self.a < other.a:
            return self.a
        else:
            return other
    def __gt__(self, other):

        if self.a > other.a:
            return self
        return other


def helper(line1,line2, our_bazeh):

    d = (line1.b - line2.b) / (line2.a - line1.a)

    if our_bazeh[0] < d and d > our_bazeh[1]:

        return [[min(line1,line2),[our_bazeh[0],d]],[max(line1,line2),[d,our_bazeh[1]]]]
    elif d <= our_bazeh[0]:
        return [[max(line1,line2),our_bazeh]]
    elif d >= our_bazeh[1]:
        return [[min(line1,line2),our_bazeh]]

def marge(left,right):

    pointer1 = pointer2 = 0
    size_1 = len(left)
    size_2 = len(right)
    list_result = []
    while pointer1 < size_1 and pointer2 < size_2:

        right_item = right[pointer2]
        left_item  = left[pointer1]

        our_bazeh = [right_item[1][0],min(right_item[1][1],left_item[1][1])]
        list_result.append(helper(left_item[0],right_item[0],our_bazeh))

        if right[1][1] < left[1][1]:

            pointer2 += 1

            left[pointer1][1] = [right_item[1][1],left_item[1],1]

        elif right_item[1][1] > left_item[1][1]:

            pointer1 += 1

            right[pointer2][1] = [left_item[1][1],right_item[1],1]

        else :

            pointer1 += 1
            pointer2 += 1


def hidden_surface_removal(list_line):

    size = len(list_line)
    if size == 1:
        return [[list_line[0],[MIN,MAX]]]

    elif size == 2:

        line_1 = list_line[0]
        line_2 = list_line[1]

        if line_1 == line_2:

            if line_1.b > line_2.b:

                return [[line_1,[MIN,MAX]]]
            else:

                return [[line_2,[MIN,MAX]]]

        else:

            d = (line_1.b - line_2.b)/(line_2.a-line_1.a)

            return [[min(line_1,line_2),[MIN,d]],[max(line_1,line_2),[d,MAX]]]

    else:

        left = hidden_surface_removal(list_line[:size//2])
        right = hidden_surface_removal(list_line[size//2:])

        return marge(left,right)








def main():








if __name__ == '__main__':
    main()
