class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int [][] phon_num = {{1,2,3},{4,5,6},{7,8,9},{10,0,12}};
        int left = 10;
        int right = 12;
        int [] num_idx = {0,0};
        int [] left_idx = {0,0};
        int [] right_idx = {0,0};
        int right_distance = 0;
        int left_distance = 0;
        
        for(int number : numbers){
            //System.out.print(right);
            //System.out.println(left);
            if(number == 1 || number == 4 || number == 7){
                answer += "L";
                left = number;
            }else if(number == 3 || number == 6 || number == 9){
                answer += "R";
                right = number;
            }else{
                for(int i = 0; i < 4; i++){
                    for(int j = 0; j < 3; j++){
                        if(number == phon_num[i][j]){
                            num_idx[0] = i;
                            num_idx[1] = j;
                        }
                        if(right == phon_num[i][j]){
                            right_idx[0] = i;
                            right_idx[1] = j;
                        }else if(left == phon_num[i][j]){
                            left_idx[0] = i;
                            left_idx[1] = j;
                        }
                    }
                }
                right_distance = Math.abs(num_idx[0]-right_idx[0]) + Math.abs(num_idx[1]-right_idx[1]);
                left_distance = Math.abs(num_idx[0]-left_idx[0]) + Math.abs(num_idx[1]-left_idx[1]);
                if (right_distance > left_distance){
                    answer += "L";
                    left = number;
                }
                else if(right_distance < left_distance){
                    answer += "R";
                    right = number;
                }
                else{
                    if (hand.equals("right")){
                        answer += "R";
                        right = number;
                    }else{
                        answer += "L";
                        left = number;
                    }
                }
            }
        }
        System.out.println(answer);
        return answer;
    }
}
/*
1. �޴�����ȣ�� 2�����迭�� ����� ù��°���� �ε��� 0, �ι�° ���� �ε��� 1������ �����Ѵ�.
2. ���� �޼հ� ������ ��ġ�� ������ ������ ����� ��ȣ�� ���������� ������ġ�� �ʱ�ȭ�Ѵ�.
3. ������ġ���� �������� ���ڰ� �Ÿ��� ���밪���� ����
4. ���밪�� ���Ͽ� �� �������� ������ ����, but ������ hand������ ������ ����
*/