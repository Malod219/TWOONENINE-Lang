# TWOONENINE-Lang
Assembly-like language interpreter
## About and Intention
TWOONENINE-Lang is an assembly-like  language. The intention is to make it easier to write in an "assembly-like" way, with some higher level constructions possible, such as Data Structures. I may write a compiler for this language later on to achieve a later intention. I may also add "time calculating" capabilities baked into the instruction set. The intention of this language is to be a simple language that is easily understood. The later intention that may become evident, is for this language to be possible to use for writing algorithms and testing them experimentally, without the overhead of "JIT Compilers" or "Interpretation".

## Architecture
TWOONENINE-Lang is intended to be an assembly-like language that makes implementing data-structures easier. The following is the architecture:
NODEs can locally store their own Data and have their own local accumulator. They can also be used to pass data to other NODEs.
`dat0-dat15` can store integers or strings.
`acc` can store integers or strings. All subtraction, and conditional logic operates on the value in the accumulator
## InstructionSet
- NODE `number` - Create a NODE. Currently, only NODE 0 does anything, and operates as where the code is run from.
- LABEL `labelName` - Create a LABEL. LabelNames must be fully connected names without spacing.
- SUB `number` - Subtract a number from the Accumulator.
- MOV `register` `number` - Move a number into a register.
- MOV `register` `register` - Move the contents of a register to another register.
- MOV `register` str `string` - Move a single fully connected String into the register.
- MOV `register` inp - Move contents from user input into the Register. USER INPUT MUST BE INTEGERS.
- MOV `register` out - Output the contents of Register to the screen.
- JGZ `labelName` - Move from current line to the line at the label corresponding with that labelname if acc > 0.
- JEZ `labelName` - Move from current line to the line at the label corresponding with that labelname if acc == 0.
- JLZ `labelName` - Move from current line to the line at the label corresponding with that labelname if acc < 0.
## Syntax rules
- All instruction names MUST be fully capitalised. No `mov` or `mOv`.
- All register names MUST be lower case. No `Dat0` or `DAT4`.
- No indentation.
- Commenting and empty lines is fine.
- Commenting can be done by just writing, though it is recommended to prefix all comments with `# `.
## Contributing
I encourage contribution. Feel free to write a compiler or interpreter for this language, or modify the language to have more instructions or syntax rules. License: MIT License

©RisingThumb 2019
