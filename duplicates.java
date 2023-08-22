import java.util.HashSet;
import java.util.Set;

public class Solution {
    public boolean contrainDuplicates(int[] nums) {
        Set<Integer> hashset = new HashSet<>();

        for (int i : nums) {
            if (hashset.contains(i)) {
                return true;
            }
            hashset.add(i);
        }
        return false;
    }
}