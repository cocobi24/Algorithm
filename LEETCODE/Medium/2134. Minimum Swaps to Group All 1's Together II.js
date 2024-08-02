// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/?envType=daily-question&envId=2024-08-02

let minSwaps = function(nums) {
    let total = 0;
    for (let i=0; i < nums.length; i++) {
        if (nums[i] == 1) {
            total += 1;
        }
    }
    let circle = nums.concat(nums);
    let answer = 999999999;
    
    let l = 0;
    let r = total - 1;
    let sm = 0;
    for (let i=l; i < r + 1; i++) {
        sm += circle[i];
    }

    answer = answer > r - l + 1 - sm ? r - l + 1 - sm : answer;
    while (r < circle.length-1) {
        sm -= circle[l];
        l += 1;
        sm += circle[r+1];
        r += 1;
        answer = answer > r - l + 1 - sm ? r - l + 1 - sm : answer;
    }
    return answer;
};