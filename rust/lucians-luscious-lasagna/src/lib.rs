// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

const expected_oven_time: i32 = 40;

const time_per_layer: i32 = 2;

pub fn expected_minutes_in_oven() -> i32 {
    expected_oven_time
}

pub fn remaining_minutes_in_oven(actual_minutes_in_oven: i32) -> i32 {
    expected_oven_time - actual_minutes_in_oven
}

pub fn preparation_time_in_minutes(number_of_layers: i32) -> i32 {
    time_per_layer * number_of_layers
}

pub fn elapsed_time_in_minutes(number_of_layers: i32, actual_minutes_in_oven: i32) -> i32 {
    (number_of_layers * time_per_layer) + actual_minutes_in_oven
}
