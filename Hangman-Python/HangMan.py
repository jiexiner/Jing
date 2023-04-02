
from random import choice, random



def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    for key in range(1,max_size+1):
        dictionary[key]=[]

    with open(filename,'r') as file:
        for line in file:
            for word in line.split():
                word = word.upper()
                try:
                    length = len(word)
                    dictionary[length].append(word)
                except:
                    length = 12
                    dictionary[length].append(word)
    return dictionary


def print_dictionary (dictionary) :
    print(dictionary)


def get_game_options_size(size):
    
    try:
        words = choice(dictionary[int(size)])
        print('The word size is set to '+str(size)+'.')
    except:
        size = choice(range(3,13))
        words = choice(dictionary[int(size)])
        print('A dictionary word of any size will be chosen.')
    return (size,words)


def get_game_options_lives(lives):
    
    try:
        int(lives)
        if int(lives)>0 and int(lives)<11:
            lives = lives
        else:
            lives = 5       
    except ValueError:
        lives = 5
    print('You have '+str(lives)+' lives.')
    return lives



if __name__ == '__main__' :
    dictionary_file= "dictionary-short.txt"
    dictionary = import_dictionary(dictionary_file)
    print('Welcome to the Hangman Game!')
    n=0
    test_list = []
    alpha = 'A'
    for i in range(0, 26):
        test_list.append(alpha)
        alpha = chr(ord(alpha) + 1)
    while n==0:
        size = input('Please choose a size of a word to be guessed [3 - 12, default any size]:'+'\n')
        size = get_game_options_size(size)
        lives = input('Please choose a number of lives [1 - 10, default 5]:'+'\n')
        lives = get_game_options_lives(lives)
        lc_list= ['Letters','chosen:']
        ori_live = lives
        word = size[1]
        
        word_list = list(size[1])

    
    
        letter_list = []
        length = len(word_list)
        us = '__'
        nd_list = []
        nd_list.extend([us for i in range(int(size[0]))])
        if '-' in word_list:
            nd_list[word_list.index('-')] = '-'
        else:
            pass
        nd = '  '.join(nd_list)
        li = 'O'
        live_list = []
        live_list.extend([li for i in range(int(lives))])
        lis = ''.join(live_list)
        print(' '.join(lc_list)+' ')
        print(nd+'   lives: '+str(lives)+' '+lis)
        q=0
        m=1
    
        while q==0:
            
            user_letter = input('Please choose a new letter >'+'\n').upper()
            letter = ''
            
            if user_letter in word_list and not user_letter in letter_list and user_letter in test_list:
                letter_list.append(user_letter)
                letter = ', '.join(letter_list)
            
                print('You guessed right!')
                matched_indexes = []
                i=0
                while i<length:
                
                    if user_letter == word_list[i]:
                        matched_indexes.append(i)              
                    i+=1
                mtlength = len(matched_indexes)
                z=0
                while z<mtlength:
                    nd_list[int(matched_indexes[z])] = user_letter
                    z+=1
                print(' '.join(lc_list)+' '+letter)
                print('  '.join(nd_list)+'   lives: '+str(lives)+' '+lis)
        
            else:
                if not user_letter in test_list:
                    pass
                elif len(user_letter) != 1:
                    pass
                elif not user_letter in letter_list:
                    letter_list.append(user_letter)
                    letter = ', '.join(letter_list)
                    lives =int(lives)-1
                    live_list[int(m-1)] = 'X'
                    lis=''.join(live_list)
                    m+=1
                    print('You guessed wrong, you lost one life.')
                    print(' '.join(lc_list)+' '+letter)
                    print('  '.join(nd_list)+'   lives: '+str(lives)+' '+lis)
                
                else:
                    letter = ', '.join(letter_list)
                    print('You have already chosen this letter.')
            
            if not '__' in nd_list:
                q=1
                print('Congratulations!!! You won! The word is '+word+'!')
                user_input = input('Would you like to play again [Y/N]?'+'\n').upper()
                if user_input == 'Y':
                    n=0
                else:
                    n=1
                    print('Goodbye!')
                    break
            elif lives == 0:
                q=1
                print('You lost! The word is '+word+'!')
                user_input = input('Would you like to play again [Y/N]?'+'\n').upper()
                if user_input == 'Y':
                    n=0
                else:
                    n=1
                    print('Goodbye!')
                    break                
            else:
                pass
