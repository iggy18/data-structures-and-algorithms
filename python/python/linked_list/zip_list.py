from linked import Node, LinkedList

def zip_lists(first, second):
    ll_a = first.head
    zip_a = ll_a.next
    ll_b = second.head
    zip_b = ll_b.next

    while ll_a and ll_b:
        ll_a.next = ll_b
        ll_b.next = zip_a
        ll_a = ll_b.next
        zip_b = ll_a.next
        ll_a.next = ll_b
        zip_a = zip_a.next
        zip_b = zip_b.next
    return first
