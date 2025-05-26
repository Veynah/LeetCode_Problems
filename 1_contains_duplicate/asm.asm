section .data
    hash_table times 4096 dd -1    ; 4096 cases initialisées à -1 (vide)
    table_size equ 4096            ; taille de la table (puissance de 2)

section .text
global hasDuplicate
hasDuplicate:
    ; Arguments:
    ; eax = pointeur vers tableau nums
    ; ebx = taille du tableau

    push ebp
    mov ebp, esp
    push esi
    push edi
    push ecx
    push edx

    xor ecx, ecx              ; ecx = index du tableau nums
.loop:
    cmp ecx, ebx              ; tant que ecx < taille
    jge .no_duplicate

    mov esi, [eax + ecx*4]    ; esi = nums[ecx]
    ; Hash: esi mod table_size
    mov edi, esi
    and edi, table_size - 1   ; edi = hash index (modulo table_size)

.probe:
    mov edx, [hash_table + edi*4]
    cmp edx, -1               ; case vide ?
    je .insert                ; si vide => on insère

    cmp edx, esi              ; même valeur ?
    je .found_duplicate       ; si oui => doublon trouvé

    inc edi
    and edi, table_size - 1   ; wrap autour (modulo)
    jmp .probe

.insert:
    mov [hash_table + edi*4], esi ; insère la valeur
    inc ecx
    jmp .loop

.found_duplicate:
    mov eax, 1                ; return true
    jmp .exit

.no_duplicate:
    xor eax, eax              ; return false

.exit:
    pop edx
    pop ecx
    pop edi
    pop esi
    pop ebp
    ret

