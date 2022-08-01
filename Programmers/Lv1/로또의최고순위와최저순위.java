class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0};
        int[] winning_num = {0,0}; //��÷������ ���� ������ �ְ����� ���� �迭
        for(int lotto : lottos){
            if (lotto == 0){
                winning_num[0] += 1; //lotto���� 0�̸� �������� �߰�
            }
            else {
                for(int win_num : win_nums){
                    if (lotto == win_num){
                        winning_num[0] += 1; //lotto���� ��÷��ȣ�� ���ԵǸ� ���������� �ְ��� �߰�
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
1. win_nums�� ��ȸ�ϸ鼭 �� ���ڰ� lottos����Ʈ�� �ִ��� Ȯ���Ͽ� ������ ��ġ�� ����
2. ���� ��ġ�ϴ� ��ȣ ���� -> ��������, ������ġ ��ȣ + 0 ���� -> �ְ������� ����� �� ����
3. ������ ����, �ְ����� ����Ʈ�� ��ȯ��
*/