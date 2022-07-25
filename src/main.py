import requests
import sys

def get_rhymes(word: str) -> list[str]:
    params = {'function': 'getRhymes', 'word': word, 'lang': 'en', 'maxResults': 100}
    result = requests.get('https://rhymebrain.com/talk', params=params).json()
    return [x['word'] for x in result if x['score'] >= 100]

def rhymes_list_to_str(rhymes: list[str]) -> str:
    return ', '.join(rhymes)

if __name__ == '__main__':
    word: str
    if len(sys.argv) == 2:
        word = sys.argv[1]
    else:
        word = input("Enter word: ")
        
    print(rhymes_list_to_str(get_rhymes(word)))