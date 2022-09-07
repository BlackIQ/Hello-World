// Part of the Carbon Language project, under the Apache License v2.0 with LLVM
// Exceptions. See /LICENSE for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
// RUN: %{explorer} %s 2>&1 | \
// RUN:   %{FileCheck} --match-full-lines --allow-unused-prefixes=false %s
// RUN: %{explorer} --parser_debug --trace_file=- %s 2>&1 | \
// RUN:   %{FileCheck} --match-full-lines --allow-unused-prefixes %s
// AUTOUPDATE: %{explorer} %s
// CHECK: Hello world!
// CHECK: result: 0

package ExplorerTest api;

//fn is function declaration
//return type is i32 i.e. int.

fn Main() -> i32 {
  var s: auto = "Hello world!"; // Auto Variable
  let x: i32 = 20; // Constant
  var y: i32 = 3; // Integer variable 
  Print(s); // Print 
  return 0; //Return value 
}