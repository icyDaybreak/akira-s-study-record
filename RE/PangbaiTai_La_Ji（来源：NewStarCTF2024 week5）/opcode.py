program=[0x01, 0x00, 0x00, 0x08, 0x00, 0x18, 0x0A, 0x23, 0x02, 0x01, 
  0x80, 0x00, 0x04, 0x01, 0x00, 0x01, 0x05, 0x01, 0x80, 0x01, 
  0x0B, 0x02, 0x01, 0x06, 0x02, 0x00, 0x02, 0x03, 0x80, 0x00, 
  0x02, 0x07, 0x00, 0x09, 0x03, 0xFF]

# | opcode | 指令                   | 语义                                    |
# | ------ | ---------------------- | --------------------------------------- |
# | 1      | LOAD_IMM op1,op2       | op2->R[op1]                             |
# | 2      | LOAD_ADDR op1,op2,op3  | R[R[op3]+op2]->R[op1]                   |
# | 3      | STORE_ADDR op1,op2,op3 | R[op3]->(R[op2]+op1)                    |
# | 4      | ADD op1,op2,op3        | R[op1]+R[op2]->R[op3]                   |
# | 5      | MOD op1,op2,op3        | R[op1]%op2->R[op3]                      |
# | 6      | XOR op1,op2,op3        | R[op1]^R[op2]->R[op3]                   |
# | 7      | INC op1                | R[op1]+1->R[op1]                        |
# | 8      | CMP op1,op2            | (R[op1]==op2)->Flag                     |
# | 9      | JMP op1                | op1->PC                                 |
# | A      | JNZ op1                | if FLAG != 0 then PC = op1 else PC += 2 |
# | B      | LOAD_IND op1, op2      | R[op1]<-(R[op2])                        |

def disasm(code):
    pc = 0
    out = []
    while pc < len(code):
        op = code[pc]

        if op == 0x01:   # LOAD_IMM
            r = code[pc+1]
            imm = code[pc+2]
            out.append(f"{pc:02X}: LOAD_IMM R{r}, {imm}")
            pc += 3

        elif op == 0x02: # LOAD_ADDR
            r = code[pc+1]
            imm = code[pc+2]
            base = code[pc+3]
            out.append(f"{pc:02X}: LOAD_ADDR R{r}, {imm}, R{base}")
            pc += 4

        elif op == 0x03: # STORE_ADDR
            off = code[pc+1]
            base = code[pc+2]
            src  = code[pc+3]
            out.append(f"{pc:02X}: STORE_ADDR {off}, R{base}, R{src}")
            pc += 4

        elif op == 0x04: # ADD
            r1 = code[pc+1]
            r2 = code[pc+2]
            rd = code[pc+3]
            out.append(f"{pc:02X}: ADD R{r1}, R{r2}, R{rd}")
            pc += 4

        elif op == 0x05: # MOD
            r = code[pc+1]
            imm = code[pc+2]
            rd = code[pc+3]
            out.append(f"{pc:02X}: MOD R{r}, {imm}, R{rd}")
            pc += 4

        elif op == 0x06: # XOR
            r1 = code[pc+1]
            r2 = code[pc+2]
            rd = code[pc+3]
            out.append(f"{pc:02X}: XOR R{r1}, R{r2}, R{rd}")
            pc += 4

        elif op == 0x07: # INC
            r = code[pc+1]
            out.append(f"{pc:02X}: INC R{r}")
            pc += 2

        elif op == 0x08: # CMP
            r = code[pc+1]
            imm = code[pc+2]
            out.append(f"{pc:02X}: CMP R{r}, {imm}")
            pc += 3

        elif op == 0x09: # JMP
            imm = code[pc+1]
            out.append(f"{pc:02X}: JMP {imm}")
            pc += 2

        elif op == 0x0A: # JNZ
            imm = code[pc+1]
            out.append(f"{pc:02X}: JNZ {imm}")
            pc += 2

        elif op == 0x0B: # LOAD_IND
            rd = code[pc+1]
            rs = code[pc+2]
            out.append(f"{pc:02X}: LOAD_IND R{rd}, R{rs}")
            pc += 3

        else:
            out.append(f"{pc:02X}: DB {op}")
            pc += 1

    return out


for line in disasm(program):
    print(line)
