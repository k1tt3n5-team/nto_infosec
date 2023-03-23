from sage.all import *


class DihedralCrypto:
    def __init__(self) -> None:
        self.__G = DihedralGroup(1337)
        self.__gen = self.__G.gens()[0]
        self.__list = self.__G.list()

    def __pow(self, element, exponent: int):
        try:
            element = self.__G(element)
        except:
            raise Exception("Not Dihedral rotation element")
        answer = self.__G(())
        aggregator = element
        for bit in bin(int(exponent))[2:][::-1]:
            if bit == '1':
                answer *= aggregator
            aggregator *= aggregator
        return answer

    def __byte_to_dihedral(self, byte: int):
        return self.__pow(self.__gen, byte * 31337)

    def __map(self, element):
        return self.__list.index(element)

    def __unmap(self, index):
        return self.__list[index]

    def hash(self, msg):
        answer = []
        for byte in msg:
            answer.append(self.__map(self.__byte_to_dihedral(byte)))
        return answer

    def unhash(self, msg):
        for byte in msg:
            ans = self.__unmap(byte)
            for i in range(256):
                answer = self.__G(())
                aggregator = self.__G(self.__gen)
                for bit in bin(int(i * 31337))[2:][::-1]:
                    if bit == '1':
                        answer *= aggregator
                    aggregator *= aggregator

                if answer == ans:
                    print(chr(i), end='')


data = [277, 92, 775, 480, 160, 92, 31, 586, 277, 801, 355, 489, 801, 31, 62, 926, 725, 489, 160, 92, 31, 586, 277, 801,
        355, 489, 1281, 62, 801, 489, 1175, 277, 453, 489, 453, 348, 725, 31, 348, 864, 864, 348, 453, 489, 737, 288,
        453, 489, 889, 804, 96, 489, 801, 721, 775, 926, 1281, 631]

if __name__ == "__main__":
    dihedral = DihedralCrypto()
    dihedral.unhash(data)
