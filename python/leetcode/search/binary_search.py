def find_larger(arr, nums):
  print 'array in order: ', arr
  print 'nums to look up nearest larger: ', nums
  # arr.append(float('inf'))
  for tmp_num in nums:
    st_id = 0
    end_id = len(arr) - 1
    mid_id = (st_id + end_id) / 2
    while(st_id<mid_id):
      # print mid_id
      if tmp_num >= arr[mid_id]:
        st_id = mid_id
      else:
        end_id = mid_id
      mid_id = (st_id + end_id) / 2
    if tmp_num < arr[st_id]:
      print tmp_num, arr[st_id]
    elif tmp_num < arr[end_id]:
      print tmp_num, arr[end_id]
    else:
      print tmp_num, '-'

def find_nearest(arr, nums):
  print 'array in order: ', arr
  print 'nums to look up: ', nums
  # arr.append(float('inf'))
  for tmp_num in nums:
    st_id = 0
    end_id = len(arr) - 1
    mid_id = (st_id + end_id) / 2
    while(st_id<mid_id):
      # print mid_id
      if tmp_num == arr[mid_id]:
        st_id = mid_id
        break
      elif tmp_num > arr[mid_id]:
        st_id = mid_id
      else:
        end_id = mid_id
      mid_id = (st_id + end_id) / 2
    if tmp_num - arr[st_id] < arr[end_id] - tmp_num:
      print tmp_num, arr[st_id]
    else:
      print tmp_num, arr[end_id]


if __name__ == '__main__':
  # find_nearest([1,3,5,7,9], [-1, 3, 6, 8,9,100])
  # find_larger([1,3,5,7,9], [-1, 3, 6, 8,9,100])
  find_smaller([1,3,5,7,9], [-1, 3, 6, 8,9,100])

