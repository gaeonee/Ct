class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0};
        int[] winning_num = {0,0}; //당첨가능한 최저 갯수와 최고갯수를 담을 배열
        for(int lotto : lottos){
            if (lotto == 0){
                winning_num[0] += 1; //lotto값이 0이면 최저갯수 추가
            }
            else {
                for(int win_num : win_nums){
                    if (lotto == win_num){
                        winning_num[0] += 1; //lotto값이 당첨번호에 포함되면 최저갯수와 최고갯수 추가
                        winning_num[1] += 1;
                    }
                }
            }
        }
        for(int rank = 0; rank<2; rank++){
            switch(winning_num[rank]){
                case 6 : answer[rank] = 1; break;
                case 5 : answer[rank] = 2; break;
                case 4 : answer[rank] = 3; break;
                case 3 : answer[rank] = 4; break;
                case 2 : answer[rank] = 5; break;
                default : answer[rank] = 6; break;
            }
        }
        return answer;
    }
}
/*
1. win_nums를 순회하면서 각 숫자가 lottos리스트에 있는지 확인하여 있으면 일치값 증가
2. 기존 일치하는 번호 갯수 -> 최저점수, 기존일치 번호 + 0 갯수 -> 최고점수로 계산할 수 있음
3. 구해진 최저, 최고점수 리스트를 반환함
*/