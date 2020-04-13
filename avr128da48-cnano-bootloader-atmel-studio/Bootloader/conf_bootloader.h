/**
 * \file conf_bootloader.h
 *
 * \brief Bootloader configuration file.
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

#ifndef CONF_BOOTLOADER_H_INCLUDED
#define CONF_BOOTLOADER_H_INCLUDED

#include <stdint.h>
#include <avr/io.h> 

#define BOOTSIZE_FUSE               (0x02)
#define BOOT_SIZE                   (BOOTSIZE_FUSE * PROGMEM_PAGE_SIZE)
#define APPCODE_START               BOOT_SIZE

#define BOOTLOADER_START_MARK       0x494E464F      // "INFO" tag
#define BOOTLOADER_IMG_START_MARK   0x53545830      // "STX0" tag
#define MARK_SIZE                   4

typedef struct
{
    uint32_t start_mark;
    uint32_t start_address;
    uint32_t memory_size;
    uint8_t  reserved[116];                      
}application_code_info;


#endif /* CONF_BOOTLOADER_H_INCLUDED */
