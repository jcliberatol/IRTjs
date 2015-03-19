{
  "targets": [
    {
      "target_name": "hello",
      "sources": [ "hello.cpp" , "interface.h"],
      "include_dirs": ["IRT/SICS/src"],
      "cflags": ["-std=c++11"],
      "cflags_cc!": ['-fno-rtti'],
      "cflags_cc+": ['-frtti']

    }
  ]
}
