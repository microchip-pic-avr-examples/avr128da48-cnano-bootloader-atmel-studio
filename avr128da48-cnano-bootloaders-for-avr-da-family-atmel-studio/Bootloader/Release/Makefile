################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL := cmd.exe
RM := rm -rf

USER_OBJS :=

LIBS := 
PROJ := 

O_SRCS := 
C_SRCS := 
S_SRCS := 
S_UPPER_SRCS := 
OBJ_SRCS := 
ASM_SRCS := 
PREPROCESSING_SRCS := 
OBJS := 
OBJS_AS_ARGS := 
C_DEPS := 
C_DEPS_AS_ARGS := 
EXECUTABLES := 
OUTPUT_FILE_PATH :=
OUTPUT_FILE_PATH_AS_ARGS :=
AVR_APP_PATH :=$$$AVR_APP_PATH$$$
QUOTE := "
ADDITIONAL_DEPENDENCIES:=
OUTPUT_FILE_DEP:=
LIB_DEP:=
LINKER_SCRIPT_DEP:=

# Every subdirectory with source files must be described here
SUBDIRS := 


# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS +=  \
../boot.c


PREPROCESSING_SRCS +=  \
../flash_access.S


ASM_SRCS += 


OBJS +=  \
boot.o \
flash_access.o

OBJS_AS_ARGS +=  \
boot.o \
flash_access.o

C_DEPS +=  \
boot.d \
flash_access.d

C_DEPS_AS_ARGS +=  \
boot.d \
flash_access.d

OUTPUT_FILE_PATH +=AVR-Dx_Bootloader.elf

OUTPUT_FILE_PATH_AS_ARGS +=AVR-Dx_Bootloader.elf

ADDITIONAL_DEPENDENCIES:=

OUTPUT_FILE_DEP:= ./makedep.mk

LIB_DEP+= 

LINKER_SCRIPT_DEP+= 


# AVR32/GNU C Compiler
./boot.o: .././boot.c
	@echo Building file: $<
	@echo Invoking: AVR/GNU C Compiler : 5.4.0
	$(QUOTE)C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-gcc.exe$(QUOTE)  -x c -funsigned-char -funsigned-bitfields -DNDEBUG  -I"C:\Program Files (x86)\Atmel\Studio\7.0\Packs\Atmel\AVR-Dx_DFP\1.0.11\include" -I"C:\Program Files (x86)\Atmel\Studio\7.0\Packs\Atmel\AVR-Dx_DFP\1.0.18\include"  -Os -ffunction-sections -fdata-sections -fpack-struct -fshort-enums -Wall -mmcu=avr128da48 -B "C:\Program Files (x86)\Atmel\Studio\7.0\Packs\Atmel\AVR-Dx_DFP\1.0.18\gcc\dev\avr128da48" -c -std=gnu99 -MD -MP -MF "$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)"   -o "$@" "$<" 
	@echo Finished building: $<
	




# AVR32/GNU Preprocessing Assembler



# AVR32/GNU Assembler
./flash_access.o: .././flash_access.S
	@echo Building file: $<
	@echo Invoking: AVR/GNU Assembler : 5.4.0
	$(QUOTE)C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-gcc.exe$(QUOTE) -Wa,-gdwarf2 -x assembler-with-cpp -c -mmcu=avr128da48 -B "C:\Program Files (x86)\Atmel\Studio\7.0\Packs\Atmel\AVR-Dx_DFP\1.0.18\gcc\dev\avr128da48" -I "C:\Program Files (x86)\Atmel\Studio\7.0\Packs\Atmel\AVR-Dx_DFP\1.0.11\include" -I "C:\Program Files (x86)\Atmel\Studio\7.0\Packs\Atmel\AVR-Dx_DFP\1.0.18\include"  -MD -MP -MF "$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)"   -o "$@" "$<" 
	@echo Finished building: $<
	





ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: $(OUTPUT_FILE_PATH) $(ADDITIONAL_DEPENDENCIES)

$(OUTPUT_FILE_PATH): $(OBJS) $(USER_OBJS) $(OUTPUT_FILE_DEP) $(LIB_DEP) $(LINKER_SCRIPT_DEP)
	@echo Building target: $@
	@echo Invoking: AVR/GNU Linker : 5.4.0
	$(QUOTE)C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-gcc.exe$(QUOTE) -o$(OUTPUT_FILE_PATH_AS_ARGS) $(OBJS_AS_ARGS) $(USER_OBJS) $(LIBS) -nostartfiles -Wl,-Map="AVR-Dx_Bootloader.map" -Wl,--start-group -Wl,-lm  -Wl,--end-group -Wl,--gc-sections -mmcu=avr128da48 -B "C:\Program Files (x86)\Atmel\Studio\7.0\Packs\Atmel\AVR-Dx_DFP\1.0.18\gcc\dev\avr128da48"  
	@echo Finished building target: $@
	"C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-objcopy.exe" -O ihex -R .eeprom -R .fuse -R .lock -R .signature -R .user_signatures  "AVR-Dx_Bootloader.elf" "AVR-Dx_Bootloader.hex"
	"C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-objcopy.exe" -j .eeprom  --set-section-flags=.eeprom=alloc,load --change-section-lma .eeprom=0  --no-change-warnings -O ihex "AVR-Dx_Bootloader.elf" "AVR-Dx_Bootloader.eep" || exit 0
	"C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-objdump.exe" -h -S "AVR-Dx_Bootloader.elf" > "AVR-Dx_Bootloader.lss"
	"C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-objcopy.exe" -O srec -R .eeprom -R .fuse -R .lock -R .signature -R .user_signatures "AVR-Dx_Bootloader.elf" "AVR-Dx_Bootloader.srec"
	"C:\Program Files (x86)\Atmel\Studio\7.0\toolchain\avr8\avr8-gnu-toolchain\bin\avr-size.exe" "AVR-Dx_Bootloader.elf"
	
	





# Other Targets
clean:
	-$(RM) $(OBJS_AS_ARGS) $(EXECUTABLES)  
	-$(RM) $(C_DEPS_AS_ARGS)   
	rm -rf "AVR-Dx_Bootloader.elf" "AVR-Dx_Bootloader.a" "AVR-Dx_Bootloader.hex" "AVR-Dx_Bootloader.lss" "AVR-Dx_Bootloader.eep" "AVR-Dx_Bootloader.map" "AVR-Dx_Bootloader.srec" "AVR-Dx_Bootloader.usersignatures"
	