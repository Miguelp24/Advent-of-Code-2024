def calcChecksum(start_block_id, num_blocks, file_old_pos):
  # a = start_block_id                  : Lowest Block ID
  # b = start_block_id + num_blocks - 1 : Highest Block ID
  # (b + a)(b - a + 1)/2                : Sum of block IDs
  # file_old_pos/2                      : File ID
  # Sum (Block IDs * File ID) = (Sum Block IDs) * File ID
  # which simplifies to:
  return (2*start_block_id + num_blocks - 1) * num_blocks * file_old_pos // 4
 
# Part 1
def Part1(data): 
  front_pos = 0
  back_pos = len(data)-1
  
  passed_blocks = 0
  front_blocks = int(data[front_pos])
  back_blocks = int(data[back_pos])
  
  checksum = 0
  
  while front_pos < back_pos:
      if front_pos % 2 == 0:
          checksum += calcChecksum(passed_blocks, front_blocks, front_pos)
          passed_blocks += front_blocks
          
          front_pos += 1
          front_blocks = int(data[front_pos])
      else:
          if back_blocks >= front_blocks:
              checksum += calcChecksum(passed_blocks, front_blocks, back_pos)
  
              passed_blocks += front_blocks
              back_blocks -= front_blocks
  
              front_pos += 1
              front_blocks = int(data[front_pos])
          else:
              checksum += calcChecksum(passed_blocks, back_blocks, back_pos)
  
              passed_blocks += back_blocks
              front_blocks -= back_blocks
  
              back_pos -= 2
              back_blocks = int(data[back_pos])
  
  if back_pos == front_pos:
      remaining_blocks = min(front_blocks, back_blocks)
      checksum += calcChecksum(passed_blocks, remaining_blocks, front_pos)
  
  return(checksum)
 
# Part 2
def Part2(data): 
  free = {}
  pos = {}
  passed_blocks = 0
  i = 1
  
  while i < len(data):
      pos[i-1] = passed_blocks
      passed_blocks += int(data[i-1])
      free_blocks = int(data[i])
      free[i] = (passed_blocks, free_blocks)
      passed_blocks += free_blocks
      i += 2
  
  i = len(data)-1
  checksum = 0
  
  while i > 1:
      num_blocks = int(data[i])
      moved = False
      for key, (start_block, space) in free.items():
          if space >= num_blocks:
              checksum += calcChecksum(start_block, num_blocks, i)
              space -= num_blocks
              if space == 0:
                  del free[key]
              else:
                  free[key] = (start_block + num_blocks, space)
              moved = True
              break
      if not moved:
          checksum += calcChecksum(pos[i], num_blocks, i)
      if i-1 in free:
          del free[i-1]
      i -= 2
  
  return(checksum)

with open('./Day-09/input.in') as file:
    input = file.read()

solution_1 = Part1(input)
solution_2 = Part2(input)

print("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)