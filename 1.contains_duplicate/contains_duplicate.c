#include <stdlib.h>
#include <string.h>
typedef struct {
  int key;
  UT_hash_handle hh;
} hash_table;

hash_table *hash = NULL, *elem, *tmp;

bool contains_duplicate(int *nums, int nums_size) {
  if (nums_size == 1) {
    return false;
  }

  bool flag = false;

  for (int i = 0; i < nums_size; i++) {
    HASH_FIND_INT(hash, &nums[i], elem);

    if (!elem) {
      elem = malloc(sizeof(hash_table));
      elem->key = nums[i];
      HASH_ADD_INT(hash, key, elem);

      flag = false;
    } else {
      flag = true;
      break;
    }
  }

  HASH_ITER(hh, hash, elem, tmp) {
    HASH_DEL(hash, elem);
    free(elem);
  }

  return flag;
}
