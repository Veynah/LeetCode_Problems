   <h1># Group Anagrams  https://leetcode.com/problems/group-anagrams/ </h1>

   <p>
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.<br>

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br>

 

Example 1:<br>

Input: strs = ["eat","tea","tan","ate","nat","bat"]<br>
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]<br>
Example 2:<br>

Input: strs = [""]<br>
Output: [[""]]<br>
Example 3:<br>

Input: strs = ["a"]<br>
Output: [["a"]]<br>
 

Constraints:<br>

1 <= strs.length <= 104<br>
0 <= strs[i].length <= 100<br>
strs[i] consists of lowercase English letters.<br>
   </p>

So we need to group the anagrams together, one of the methods we can use is sorting them and if they're equal to one another, then they're anagrams       of each other. <br>
 But sorting time complexity of this would be nlogn and n being the average lenght of each of the strings<br>
 and we have to do it m time, m being the number of input of strings we have to sort.<br>
 So it's m.n.log(n)<br>
 We can do better than mnlogn.<br>
 <br>
 Since the letters are only lowercase english letters, we have 26 different letters to worry about.<br>
 so what we do, is count in each string, how many letters there are of each.<br>
 eat has 1.a,1.e,1.t <br>
 tea has 1.a,1.e,1.t <br>
 tan has 1.a,1.n,1.t <br>
 ate has 1.a,1.e,1.t <br>
 nat has 1.a,1.n,1.t <br>
 bat has 1.a,1.b,1.t <br>
    
 eat, tea, ate should go together <br>
 tan and nat should go together <br>
 bat is alone <br>

 We are going to use a HashMap as our datastructure <br>
 the Key of our hashmap is going to be our pattern of count ex:1.a,1.e,1.t <br>
 And our value is the list of strings <br>

 Since we're using a Hashmap and we're counting the number of letters in our Strings <br>
 the time complexity is going to be m, the total number of input strings we're given <br>
 and n wich is the average length of our strings. So it's O(m.n) x 26, 26 being our lenght of count array <br>

 But 26 isn't counted in so it's O(m.n) <br>


