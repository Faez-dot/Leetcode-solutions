class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_w = 0
        left =0
        right=len(height)-1
        while left<right:
            width=right-left
            current_height=min(height[left], height[right])
            #Update max water vol
            current_w=width*current_height
            if current_w>max_w:
                max_w=current_w
            #point to shorter line
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_w