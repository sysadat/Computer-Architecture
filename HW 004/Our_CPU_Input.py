#create the inputs and outputs
#for an unsigned integer divider

def bit_extend(bin_num, num_bits):
  """
  extends the binary number with 0's
  until it is num_bits long
  the 0b should be removed from the binary number
  """
  return '0'* (num_bits - len(bin_num)) + bin_num

def make_CPU_inputs(outFile):
  """
  create the tests inputs for the parity checker
  """

  encodings = {'halt' : '0000',
               'nop'  : '0001',
               'load' : '0010',
               'move' : '0011',
               'andr' : '0100',
               'andi' : '0101',
               'orr'  : '0110',
               'ori'  : '0111',
               'xorr' : '1000',
               'xori' : '1001',
               'neg'  : '1011',
               'addr' : '1100',
               'addi' : '1101',
               'subr' : '1110',
               'subi' : '1111'}

  with open(outFile, 'w') as inputs:
    count = 0
    inputs.write('v3.0 raw\n')
    inputs.write(encode(encodings['load'], 0, 0, 5))  #reg0 = 5
    inputs.write(encode(encodings['load'], 1, 0, 3))  #reg1 = 3
    inputs.write(encode(encodings['nop'],  0, 0, 2))  #no change
    inputs.write(encode(encodings['move'], 2, 1, 0))  #reg2 = reg1 = 3
    inputs.write(encode(encodings['andr'], 3, 0, 1))  #reg3 = reg0 & reg1 = 5 & 3 = 1
    inputs.write(encode(encodings['andi'], 4, 3, 2))  #reg4 = reg3 & 2 = 1 & 2 = 0
    inputs.write(encode(encodings['orr'],  5, 2, 0))  #reg5 = reg2 | reg0 = 3 | 5 = 7
    inputs.write(encode(encodings['ori'],  6, 3, 10)) #reg6 = reg3 | 10 = 1 | 10 = 11
    inputs.write(encode(encodings['xorr'],  7, 3, 0))  #reg7 = reg3 ^ reg0 = 1 | 5 = 4
    inputs.write(encode(encodings['xori'], 8, 5, 6)) #reg8 = reg5 ^ 6 = 7 ^ 6 = 1 
    inputs.write(encode(encodings['neg'],  9, 5, 8))  #reg9 = -reg5 = -7
    inputs.write(encode(encodings['addr'], 10, 4, 3)) #reg10 = reg4 + reg3 = 0 + 1 = 1
    inputs.write(encode(encodings['addi'], 11, 2, 6)) #reg11 = reg2 + 6 = 3 + 6 = 9
    inputs.write(encode(encodings['subr'], 12, 5, 7)) #reg12 = reg5 - reg7 = 7 - 4 = 3
    inputs.write(encode(encodings['subi'], 13, 10, 0)) #reg13 = reg10 - 2 = 1 - 0 = 1
    inputs.write(encode(encodings['halt'], 14, 0, 7)) #halt
def encode(op, dest, reg1, reg2):
  return hex(int(op + bit_extend(bin(dest)[2:], 4) +
             bit_extend(bin(reg1)[2:], 4) +
             bit_extend(bin(reg2)[2:], 4),2))[2:] + '\n'


if __name__ == '__main__':
  make_CPU_inputs('Our_CPU_Inputs.txt')
