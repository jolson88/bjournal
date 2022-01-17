#include <stdio.h>
#include "config.h"
#include "atom.h"

int main() {
    const char *str = jmo_atom_new("hello, bjournal");
    printf("Version: %i.%i\n\n", VERSION_MAJOR, VERSION_MINOR);
    printf("%s\n", str);
    return 0;
}
