class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1)
ans1 = head
for i in range(2,6):
    ans1.next = ListNode(i)
    ans1 = ans1.next

n=2

dummy = ListNode(0)
dummy.next = head
first = dummy
second = dummy

# 先让第一个指针向前走 n+1 步
for i in range(n+1):
    first = first.next

# 然后同时移动两个指针，直到第一个指针到达末尾
while first is not None:
    first = first.next
    second = second.next

# 此时第二个指针就指向了倒数第N+1个节点
second.next = second.next.next

# return dummy.next

while head != None:
    print(head.val)
    head = head.next