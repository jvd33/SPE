#include "ruby.h"
#include <time.h>

VALUE Lab4 = Qnil;

void Init_lab4();

VALUE method_multiply(VALUE self, VALUE rb_a, VALUE rb_b);
VALUE method_hamming(VALUE self, VALUE rb_a, VALUE rb_b);
VALUE method_time_hamming(VALUE self, VALUE rb_a, VALUE rb_b, VALUE rb_n);
VALUE method_time_multiply(VALUE self, VALUE rb_a, VALUE rb_b, VALUE rb_n);

int multiply(int a, int b);
int hamming(int a, int b);

void Init_lab4() { 
    Lab4 = rb_define_class("Lab4", rb_cObject);
    rb_define_method(Lab4, "multiply", method_multiply, 2);
    rb_define_method(Lab4, "hamming", method_hamming, 2);
    rb_define_method(Lab4, "time_hamming", method_time_hamming, 3);
    rb_define_method(Lab4, "time_multiply", method_time_multiply, 3);
}

VALUE method_multiply(VALUE self, VALUE rb_a, VALUE rb_b) { 
    int a = NUM2INT(rb_a);
    int b = NUM2INT(rb_b);
    VALUE rb_result = INT2FIX(multiply(a, b));
    return rb_result;
}

VALUE method_hamming(VALUE self, VALUE rb_a, VALUE rb_b) { 
    int a = NUM2INT(rb_a);
    int b = NUM2INT(rb_b);
    VALUE rb_res = INT2FIX(hamming(a, b));
    return rb_res;
}

int multiply(int a, int b) { 
  return a * b;
}

int hamming(int a, int b) { 
  return __builtin_popcountll(a ^ b);
}

VALUE method_time_hamming(VALUE self, VALUE rb_a, VALUE rb_b, VALUE rb_n) { 
    int a = NUM2INT(rb_a);
    int b = NUM2INT(rb_b);
    int n = NUM2INT(rb_n);
    struct timeval tv1, tv2;

    gettimeofday(&tv1, NULL);
    for(int i = 0; i < n; i++) { 
        hamming(a, b);
    }
    gettimeofday(&tv2, NULL);
    double msec = (double) (tv2.tv_usec - tv1.tv_usec) / 1000000 + 
                    (double) (tv2.tv_sec - tv1.tv_sec);
    VALUE result = DBL2NUM(msec/n);
    return result;    
}

VALUE method_time_multiply(VALUE self, VALUE rb_a, VALUE rb_b, VALUE rb_n) { 
    int a = NUM2INT(rb_a);
    int b = NUM2INT(rb_b);
    int n = NUM2INT(rb_n);
    struct timeval tv1, tv2;    

    gettimeofday(&tv1, NULL);
    for(int i = 0; i < n; i++) {
        multiply(a, b);
    }
    gettimeofday(&tv2, NULL);
    double msec = (double) (tv2.tv_usec - tv1.tv_usec) / 1000000 +
                    (double) (tv2.tv_sec - tv1.tv_sec);
    VALUE result = DBL2NUM(msec/n);
    return result;
}
