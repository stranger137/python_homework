import random

print("������ ����! ������� � ����? ��������� ����� �� 1 �� 4.")
a=int(input())
r = random.randin�(1,4)
if a!=r:
    if a<r:
        print("���� ����� ������ �����������.")
    else:
        print("���� ����� ������ �����������.")
    print("��������� ��� ���!")
else:
    print("������!")