from python import *

def observer1(value):
    print("observer1:", value)

def observer2(value):
    print("observer2:", value)

def observer3(value):
    print("observer3:", value)

def test_class_observable():
    subject = Observable("123")

    print(subject)

    subject.add_observer(observer1)
    id2 = subject.add_observer(observer2)
    subject.add_observer(observer3)

    subject.set("qwer")

    subject.remove_observer(id2)

    subject.set(99)

    print(subject)

if __name__ == '__main__':
    test_class_observable()