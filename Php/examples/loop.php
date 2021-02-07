<?php

for ($i = 1; $i <= 8; $i++) {
    for ($j = 1; $j <= $i; $j++) {
        echo "*";
    }

    echo "\n";
}

// Output:
// *
// **
// ***
// ****
// *****
// ******
// *******
// ********


$fruits = ['banana', 'kiwi', 'strawberry', 'pineapple'];

echo 'My favorite fruits are: ';
foreach ($fruits as $fruit) {
    echo $fruit . " ";
}
echo "\n";

// Output:
// My favorite fruits are: banana kiwi strawberry pineapple

$number = 1;

while ($number <= 10) {
    if ($number % 2 == 0) {
        echo $number . " ";
    }

    $number++;
}
echo "\n";

// Output:
// 2 4 6 8 10
