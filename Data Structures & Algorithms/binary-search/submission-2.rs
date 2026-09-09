impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {

let mut left: i32 = 0;
let mut right: i32 = nums.len() as i32 -1 ;

while left <= right{
    let mut midpoint = (left + right )/2;

    if nums[midpoint as usize] == target{
        return midpoint;
    }
    else if nums[midpoint as usize] < target{
        left = midpoint + 1;
    } 
    else {
        right = midpoint - 1;
    }
}
 -1
    }
}
