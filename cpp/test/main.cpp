// main.cpp
// to carefully study and review how to write c++

#include <iostream>

#include "review1.h"
#include "review2.h"
#include "review3.h"
#include "dma.h"
#include "class_template.h"
#include "friends.h"
#include "nesting_template.h"
#include "functor.h"
#include "cast.h"
#include "io_test.h"

using namespace std;

int test() {
    cout << "global namespace print" << endl;
    return 1;
}


int main() {
    /*
    // test of namespace
    namespace_test();
    // global namespace
    ::test();

    // class study
    test_class1();
    test_class2();

    // Derived class study
    test_derived1();
    test_derived2();
    //polymorphic (due to virtual)
    test_derived3();

    test_friend();

    // setting class private stuff with friends classes
    test_friend_class();

    // test defining a class inside another class
    test_nesting();

    // functors study
    test_functor();

    // test type cast
    test_cast();*/

    //io_test1();
    io_test2();

    return 0;
}

