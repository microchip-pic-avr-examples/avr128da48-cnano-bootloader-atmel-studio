/**
 * \file flash_access.S
 *
 * \brief Flash access functions.
 *
 (c) 2019 Microchip Technology Inc. and its subsidiaries.
    Subject to your compliance with these terms, you may use this software and
    any derivatives exclusively with Microchip products. It is your responsibility
    to comply with third party license terms applicable to your use of third party
    software (including open source software) that may accompany Microchip software.
    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
    WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
    PARTICULAR PURPOSE.
    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
    BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
    FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
    ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
    THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *
 */

#include "utils\assembler.h"

PUBLIC_FUNCTION(pgm_jmp_far)
  
    movw    r30, r22                    // Update R30, R31 pair with address[Byte1,Byte0]
    out        _SFR_IO_ADDR(RAMPZ), r24    // Update RAMPZ with address[Byte2]
    ijmp
    ret                                 // Return to caller

END_FUNC(pgm_jmp_far)

PUBLIC_FUNCTION(pgm_word_write)

    movw    r0, r20
    movw    r30, r22                    // Update R30, R31 pair with address[Byte1,Byte0]
    out        _SFR_IO_ADDR(RAMPZ), r24    // Update RAMPZ with address[Byte2]
    spm
    clr        r1
    ret                                 // Return to caller

END_FUNC(pgm_word_write)

PUBLIC_FUNCTION(protected_write_io)

    out     _SFR_IO_ADDR(RAMPZ), r1     // Clear bits [23:16] of Z register
    movw    r30, r24                    // Load addrress into Z register
    out     CCP, r22                    // Start CCP handshake
    st      Z, r20                      // Write value to I/O register
    ret                                 // Return to caller
END_FUNC(protected_write_io)

END_FILE()
