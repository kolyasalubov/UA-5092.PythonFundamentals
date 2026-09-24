import random

SECRET_NUMBER = random.randint(1, 100)

def get_input_message(is_smaller):
  if is_smaller == None:
    return 'Type your number:'
  
  return 'Try smaller:' if is_smaller else 'Try bigger:'


def check_your_lack(is_smaller=None):
  user_beat = float(input(f'{get_input_message(is_smaller)} '))

  if user_beat == SECRET_NUMBER:
    return print('You win!')

  check_your_lack(user_beat > SECRET_NUMBER)

if __name__ == "__main__":
  check_your_lack()
