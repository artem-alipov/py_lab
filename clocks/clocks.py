import time
import os
import datetime

from views import NUMBER_TO_VIEW
 
def clear_screen():
    os.system("CLS")

def get_view(number: str):
    if len(number) == 1: 
        first = NUMBER_TO_VIEW["0"]
        second = NUMBER_TO_VIEW[number]
    else:
        first = NUMBER_TO_VIEW[number[0]]
        second = NUMBER_TO_VIEW[number[1]]
    return combine_views(first, second)

def combine_views(first, second):
    combine_numbers = [f"{first_}  {second_}" for first_, second_ in zip\
         (first.splitlines(), second.splitlines())]
    result = "\n".join(i for i in combine_numbers)
    return result

if __name__ == '__main__':
    counter = 0
    while True:
        clear_screen()
        current_time = datetime.datetime.now().time()
        hour_views = get_view(str(current_time.hour))
        minute_views = get_view(str(current_time.minute))
        second_views = get_view(str(current_time.second))

        if counter % 4 == 1:
          result = combine_views(hour_views, NUMBER_TO_VIEW[":"])
          result = combine_views(result, minute_views)
          result = combine_views(result, NUMBER_TO_VIEW[":"])
          result = combine_views(result, second_views)
          print(result)
        else:
          result = combine_views(hour_views, NUMBER_TO_VIEW["nothing"])
          result = combine_views(result, minute_views)
          result = combine_views(result, NUMBER_TO_VIEW["nothing"])
          result = combine_views(result, second_views)
          print(result)  

        time.sleep(0.2)
        counter += 1
        
