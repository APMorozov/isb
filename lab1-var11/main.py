from task1.vigenere import vigenere,decode_vigenere

if __name__ == "__main__":
    answer = vigenere('gotogym', 'goto', 'abcdefghijklmnopqrstuvwxyz')
    print(answer)
    answer2 = decode_vigenere(answer, 'goto', 'abcdefghijklmnopqrstuvwxyz')
    print(answer2)

