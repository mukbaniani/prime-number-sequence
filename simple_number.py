import numbers


class SimpleNumberList:
    @staticmethod
    def get_simple_number(number):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
            return True


    def __init__(self, number):
        if isinstance(number, numbers.Real):
            self._number_list = [num for num in range(2, number + 1) if self.get_simple_number(num)]
        elif isinstance(number, list):
            self._number_list = [num for num in number if self.get_simple_number(num)]
        else:
            self._number_list = []


    def __contains__(self, value):
        return value in self._number_list


    def __len__(self):
        return len(self._number_list)


    def __mul__(self, number):
        return SimpleNumberList(self._number_list * number)


    def __rmul__(self, number):
        return self.__mul__(number)


    def __imul__(self, number):
        self._number_list *= number
        return self


    def __add__(self, number):
        return SimpleNumberList(self._number_list + number)


    def __iadd__(self, number):
        self._number_list += number
        return self


    def __radd__(self, number):
        return self.__add__(number)


    def __getitem__(self, s):
        return self._number_list[s]


    def __delitem__(self, index):
        del self._number_list[index]


    def __setitem__(self, s, other):
        if not isinstance(other, numbers.Real):
            raise TypeError(f"{other} must be integer not {type(other)}")

        get_simple_sumber_from_other = [num for num in range(1, other + 1) if self.get_simple_number(num)]
        
        if isinstance(s, int):
            self.__reverse_append(other)
        else:
            self._number_list[s] = get_simple_sumber_from_other


    def __reverse_append(self, num):
        for n in range(num + 1, 1, -1):
            if self.get_simple_number(n):
                self._number_list.insert(0, n)


    def append(self, num):
        self._number_list.extend([n for n in range(1, num + 1) if self.get_simple_number(n)])


    def pop(self, index=-1):
        self._number_list.pop(index)


    def add_prime(self, num):
        if self.get_simple_number(num):
            self._number_list.append(num)
        else:
            raise TypeError(f"{num} must be prime number")


    def add_prime_by_index(self, number, index):
        if self.get_simple_number(number):
            self._number_list.insert(index, number)
        else:
            raise TypeError(f"{number} must be prime number")


    def __repr__(self):
        number_list_to_str = ', '.join([str(i) for i in self._number_list])
        return f"{self.__class__.__name__}({number_list_to_str})"
