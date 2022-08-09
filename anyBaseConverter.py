# a recursive function to convert decimal to ternary
def baseb(num, b):
  # case1: we can first check if input is 0
  if num == 0:
    return '0'
  # we create the quotient and remainder
  quo = num//b
  rem = num%b
  # case2: if num is not divisible by 'base', we return the remainder
  if quo == 0:
    return str(rem)
  # case3:num is divisible by 'base', we run the recursion for 
  # the 'based' representation and add the remainder to it
  else:
    return baseb(quo, b) + str(rem)
      
# Function to initiate the recursive loop
def DecimalBaseConverter(num):
  ternaryNum = ternary(num)
  return ternaryNum

if __name__ == "__main__"":
  print(DecimalBaseConverter(input()))
