// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub fn production_rate_per_hour(speed: u8) -> f64 {
    let mut success_rate = 1.0;
    if speed > 4 && speed < 9 {
        success_rate = 0.9;
    } else if speed > 8 {
        success_rate = 0.77;
    }
    speed as f64 * 221 as f64 * success_rate
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    (production_rate_per_hour(speed) / 60 as f64) as u32
}